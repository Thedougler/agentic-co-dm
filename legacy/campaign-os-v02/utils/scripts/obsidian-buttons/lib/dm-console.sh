# Sourced by scripts/obsidian-buttons/*.sh — updates a shared iTerm2 "Campaign
# OS DM Console" window on a per-role tab tailing a log file, so button output
# is watchable live instead of only reaching the DM as an Obsidian toast. The
# console is created/updated in the background: it never steals keyboard
# focus from whatever app (Obsidian) the DM is in — same frontmost-capture /
# restore idiom other buttons use, since creating an iTerm2 window can
# raise the app as a side effect of the Apple Event.
#
# dm_console_watch <role> <label> <log_file>
#   role      stable key (recording|voice|sim|scene) — persists the iTerm
#             session id at $TMPDIR/campaign-os-iterm-<role>.id so repeat
#             clicks reuse the same tab instead of stacking new ones.
#   label     tab title, e.g. "⏺ Recording".
#   log_file  path tailed with `tail -n 20 -f`; created if missing.
#
# Best-effort: iTerm2 missing/not scriptable, or the AppleScript fails for any
# reason, degrades to a stderr warning and returns 0 — callers must keep
# working with only the existing Obsidian-notification behavior.
dm_console_watch() {
  local role="$1" label="$2" log_file="$3"
  local tmp="${TMPDIR:-/tmp}"
  local window_id_file="$tmp/campaign-os-iterm-console.id"
  local session_id_file="$tmp/campaign-os-iterm-$role.id"
  local tailing_file="$tmp/campaign-os-iterm-$role.tailing"

  : >>"$log_file" 2>/dev/null || true

  local already_tailing=false
  if [[ -f "$tailing_file" && -f "$session_id_file" ]] \
    && [[ "$(cat "$tailing_file")" == "$log_file" ]]; then
    already_tailing=true
  fi

  local window_id session_id
  window_id="$( [[ -f "$window_id_file" ]] && cat "$window_id_file" || true )"
  session_id="$( [[ -f "$session_id_file" ]] && cat "$session_id_file" || true )"

  # Remember the DM's frontmost app so we can hand focus back after iTerm2
  # potentially raises itself as a side effect of window/tab creation.
  local front_app
  front_app="$(osascript -e 'tell application "System Events" to name of first process whose frontmost is true' 2>/dev/null || true)"

  local result
  if ! result="$(osascript \
      -e "on run {windowId, sessionId, tabLabel, logFile, alreadyTailing}" \
      -e 'if application "iTerm2" is not running then launch application "iTerm2"' \
      -e 'tell application "iTerm2"' \
      -e '  set targetWindow to missing value' \
      -e '  if windowId is not "" then' \
      -e '    repeat with w in windows' \
      -e '      if (id of w as string) is windowId then set targetWindow to w' \
      -e '    end repeat' \
      -e '  end if' \
      -e '  if targetWindow is missing value then set targetWindow to (create window with default profile)' \
      -e '  set targetSession to missing value' \
      -e '  tell targetWindow' \
      -e '    if sessionId is not "" then' \
      -e '      repeat with t in tabs' \
      -e '        repeat with s in sessions of t' \
      -e '          if (id of s) is sessionId then set targetSession to s' \
      -e '        end repeat' \
      -e '      end repeat' \
      -e '    end if' \
      -e '    if targetSession is missing value then' \
      -e '      set newTab to (create tab with default profile)' \
      -e '      set targetSession to (current session of newTab)' \
      -e '    end if' \
      -e '  end tell' \
      -e '  try' \
      -e '    set name of targetSession to tabLabel' \
      -e '  end try' \
      -e '  if alreadyTailing is "false" then' \
      -e '    tell targetSession to write text "clear; tail -n 20 -f " & quoted form of logFile' \
      -e '  end if' \
      -e '  return (id of targetWindow as string) & "|" & (id of targetSession)' \
      -e 'end tell' \
      -e 'end run' \
      "${window_id:-}" "${session_id:-}" "$label" "$log_file" "$already_tailing" 2>&1)"; then
    echo "DM Console unavailable (iTerm2 not installed or scripting denied) — output stays in Obsidian notifications only. $result" >&2
    return 0
  fi

  printf '%s' "${result%%|*}" >"$window_id_file"
  printf '%s' "${result##*|}" >"$session_id_file"
  printf '%s' "$log_file" >"$tailing_file"

  if [[ -n "$front_app" && "$front_app" != "iTerm2" ]]; then
    osascript -e "tell application \"System Events\" to set frontmost of process \"$front_app\" to true" >/dev/null 2>&1 || true
  fi
}
