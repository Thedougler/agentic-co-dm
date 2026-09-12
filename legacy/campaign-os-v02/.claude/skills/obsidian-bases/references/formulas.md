# Formulas

Defined in `formulas:`. Referenced as `formula.name` in `order:` and `properties:`.

```yaml
formulas:
  # Days since created
  age_days: '(now() - file.ctime).days.round(0)'

  # Conditional label
  status_icon: 'if(status == "canon", "✅", if(status == "pending", "🔄", if(status == "retired", "🗄️", "📝")))'

  # Word count estimate
  word_est: '(file.size / 5).round(0)'
```

**Key rule**: Subtracting two dates returns a `Duration`. Not a number. Always access `.days` first:
```yaml
# CORRECT
age: '(now() - file.ctime).days'

# WRONG: crashes
age: '(now() - file.ctime).round(0)'
```

**Always guard nullable properties with `if()`**:
```yaml
days_left: 'if(due_date, (date(due_date) - today()).days, "")'
```
