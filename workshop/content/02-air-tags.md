---
title: Building with Air Tags
---

Air Tags are the core building blocks for creating HTML in Air. Every standard
HTML element has a corresponding Python class in the `air` module — `air.Div`
for `<div>`, `air.Ul` for `<ul>`, `air.A` for `<a>`, and so on.

Let's expand the page to demonstrate more Air Tags. Replace the current heading
and paragraph with a richer layout that includes styled content, a list, and a
horizontal rule.

```editor:replace-matching-text
file: ~/exercises/app.py
match: |2
              air.H1("Hello, World!"),
              air.P("Welcome to the Air web framework."),
replacement: |2
              air.H1("My Air App", style="color: #2c3e50;"),
              air.P("A web application built with Air Tags."),
              air.Hr(),
              air.H2("What Are Air Tags?"),
              air.P(
                  "Air Tags are Python classes that render directly to HTML. "
                  "Each tag accepts content as positional arguments and HTML "
                  "attributes as keyword arguments."
              ),
              air.H2("Common Air Tags"),
              air.Ul(
                  air.Li("air.H1 through air.H6 for headings"),
                  air.Li("air.P for paragraphs"),
                  air.Li("air.A for links"),
                  air.Li("air.Div for containers"),
                  air.Li("air.Ul and air.Li for lists"),
              ),
```

Here is what was added:

- **`style="color: #2c3e50;"`** on the `air.H1` tag passes an HTML attribute
  as a keyword argument. Any valid HTML attribute can be set this way.

- **`air.Hr()`** renders a `<hr>` horizontal rule. Tags with no content are
  called with empty parentheses.

- **`air.H2(...)`** adds second-level headings. Air provides `air.H1` through
  `air.H6` for all heading levels.

- **`air.Ul` and `air.Li`** create an unordered list. The `air.Li` items are
  nested inside `air.Ul` as positional arguments — this is how Air Tags
  compose: outer tags wrap inner tags, mirroring HTML nesting.

- **Multi-line strings** can be used for longer text content by splitting a
  Python string across multiple lines with implicit concatenation.

The development server auto-reloads when files change. Reload the application
to see the updated page:

```dashboard:reload-dashboard
name: App
```

The page now has styled headings, descriptive text, a horizontal rule, and a
list — all built from Python code with no HTML templates.
