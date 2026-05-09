# CS50's Introduction to Programming with Python

Each problem set is implemented in **Python** and/or **Go** as a way to review Python and learn Go side-by-side.

- Python tests use [pytest](https://docs.pytest.org/)
- Go tests use the standard `go test` toolchain

---

## Language Features by Problem Set

### Week 0 — Functions

| Problem | Python | Go |
|---|---|---|
| `0_indoor` | `str.lower()`, type hints, `if __name__ == "__main__"` | `strings.ToLower`, exported functions (capitalized), package layout |
| `1_playback` | `str.replace()`, type hints | `strings.Replace` with `-1` (replace all) |
| `2_making_faces` | Chained method calls, return type annotations, Unicode literals | `strings.ReplaceAll`, intermediate variables, Unicode literals |
| `3_einstein` | Module-level constants, numeric underscores (`90_000_000_000_000_000`), `int` type hints | `const` declaration, explicit unsigned types (`uint`, `uint64`), type casting |
| `4_tip_calculator` | Custom exceptions via class inheritance, `re.fullmatch`, f-string with precision (`:.2f`), string slicing | Custom error types via `Error() string` interface, `regexp.MustCompile`, multiple return values `(T, error)`, `strconv` for type conversion |

### Week 1 — Conditionals

| Problem | Python | Go |
|---|---|---|
| `0_deep_thought` | — | `if`/`else`, logical OR (`\|\|`), string equality |
| `1_bank` | — | `strings.HasPrefix`, `strings.ToLower`, byte indexing (`s[0]`), `if`/`else if`, `strconv.Itoa` |
| `2_extensions` | — | `switch`/`case`/`default`, `regexp.MustCompile`, `FindStringSubmatch`, regex capture groups, `strings.TrimSpace` |
| `3_math_interpreter` | `re.match` with capture groups (`.group()`), `str.strip/lower/replace`, `float()`, floor division (`//`), `ZeroDivisionError`, `ValueError` | — |
| `4_meal_time` | `str.split(":")`, `float()`, numeric range checks (`>=`/`<=`), helper function for unit conversion | — |

---

## Python Features Overview

- **Type hints** — parameter and return annotations on all functions
- **String methods** — `.lower()`, `.replace()`, `.strip()`, chained calls
- **Numeric literals** — underscores for readability (`90_000_000_000_000_000`)
- **f-strings** — with format specifiers (e.g. `:.2f`)
- **Regular expressions** — `re.fullmatch` for strict matching, `re.match` with capture groups (`.group()`)
- **Floor division** — `//` operator for integer-valued results
- **Built-in exceptions** — raising `ZeroDivisionError` directly; custom exceptions via `ValueError` with messages
- **Custom exceptions** — subclassing `ValueError`, calling `super().__init__`
- **String splitting** — `str.split(":")` to unpack structured tokens
- **Module guard** — `if __name__ == "__main__"` entry point pattern
- **String slicing** — `dollars[1:]` to strip a leading character

## Go Features Overview

- **Package organization** — each problem in its own package with exported functions
- **Multiple return values** — `(T, error)` pattern for fallible operations
- **Custom error types** — named types implementing the `error` interface via `Error() string`
- **`strings` package** — `ToLower`, `HasPrefix`, `TrimSpace`, `Replace`, `ReplaceAll`
- **`regexp` package** — `MustCompile`, `MatchString`, `FindStringSubmatch` with capture groups
- **`strconv` package** — `ParseFloat`, `Itoa`, `FormatFloat` for string↔numeric conversion
- **`const`** — typed and untyped constant declarations
- **Explicit numeric types** — `uint`, `uint64`, `float32`, `float64` with explicit casts
- **`switch`/`case`** — multi-branch dispatch with a `default` fallback
- **Byte indexing** — `s[0]` to inspect the first byte of a string
- **Testing** — table-driven style using `*testing.T` and `t.Errorf`
