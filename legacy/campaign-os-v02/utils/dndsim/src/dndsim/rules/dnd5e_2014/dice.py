"""Dice-expression validation — the `parseDice` grammar (validation only;
rolling is a later slice's concern).

Grammar: one or more terms joined by ``+``/``-``, each term either ``NdX``
(``N`` optional, defaults to 1) or a flat integer, whitespace tolerated
anywhere between tokens (``"3d8 + 5"`` appears verbatim in statblocks).
Never guesses — an expression outside this grammar raises.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

_TERM_RE = re.compile(r"^([+-])?\s*(?:(\d*)d(\d+)|(\d+))\s*", re.IGNORECASE)


class DiceExprError(ValueError):
    """A dice expression is empty, non-string, or outside the grammar."""


@dataclass(frozen=True, slots=True)
class DiceTerm:
    count: int
    sides: int
    sign: int


@dataclass(frozen=True, slots=True)
class ParsedDice:
    dice: tuple[DiceTerm, ...]
    flat: int


def parse_dice_expr(expr: str) -> ParsedDice:
    """Parse ``"1d8+5"`` / ``"3d8 + 5"`` / ``"d20"`` / ``"2d6+1d4+3"`` / ``"5"``."""
    if not isinstance(expr, str) or expr.strip() == "":
        raise DiceExprError(f"dice: empty or non-string expression: {expr!r}")
    rest = expr.strip()
    dice: list[DiceTerm] = []
    flat = 0
    first = True
    while rest != "":
        m = _TERM_RE.match(rest)
        if m is None or (not first and m.group(1) is None):
            raise DiceExprError(f'dice: cannot parse "{expr}" at "{rest}"')
        sign = -1 if m.group(1) == "-" else 1
        if m.group(3) is not None:
            count_str = m.group(2)
            count = 1 if count_str in (None, "") else int(count_str)
            sides = int(m.group(3))
            if count < 1 or sides < 1:
                raise DiceExprError(f'dice: bad term in "{expr}"')
            dice.append(DiceTerm(count=count, sides=sides, sign=sign))
        else:
            flat += sign * int(m.group(4))
        rest = rest[m.end() :]
        first = False
    return ParsedDice(dice=tuple(dice), flat=flat)


def validate_dice_expr(expr: str, field: str) -> None:
    """Raise :class:`DiceExprError` naming ``field`` if ``expr`` doesn't parse."""
    try:
        parse_dice_expr(expr)
    except DiceExprError as err:
        raise DiceExprError(f"{field}: {err}") from err
