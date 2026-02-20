---
title: Workshop Summary
---

In this workshop you explored the Air web framework and learned several core
concepts for building Python web applications.

## What You Covered

- **Air Tags**: Python classes such as `air.Html`, `air.H1`, `air.P`, `air.A`,
  `air.Div`, and `air.Ul`/`air.Li` that render directly to HTML. Content is
  passed as positional arguments and HTML attributes as keyword arguments.

- **Creating an Air app**: Using `air.Air()` to create the application instance
  and decorating functions with `@app.get()` to define routes that return Air
  Tags.

- **The `@app.page` decorator**: A shortcut that automatically creates GET
  routes from function names, converting underscores to dashes in the URL path.

- **Path parameters**: Declaring parameters like `{name}` in route paths to
  build dynamic pages that respond to different URL values.

## What's Next

Air has more to offer beyond what this introductory workshop covered:

- **Jinja templates** — use `air.JinjaRenderer` to serve HTML templates
  alongside or instead of Air Tags
- **HTMX integration** — Air includes utilities for building dynamic
  interactions with HTMX
- **Pydantic form validation** — validate HTML form submissions using Pydantic
  models
- **FastAPI mounting** — mount a FastAPI app to serve a REST API alongside your
  Air web pages

Visit the [Air documentation](https://docs.airwebframework.org/) and the
[GitHub repository](https://github.com/feldroy/air) to continue learning.
