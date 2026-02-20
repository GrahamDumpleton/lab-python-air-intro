---
title: Adding Routes
---

So far the application has a single route. Let's add more pages and link them
together.

## The About Page

Add an about page using the `@app.page` decorator. Unlike `@app.get()` which
requires an explicit path, `@app.page` automatically generates the route from
the function name — a function named `about` creates the route `/about`.

```editor:append-lines-to-file
file: ~/exercises/app.py
text: |4


    @app.page
    def about():
        return air.Html(
            air.Head(air.Title("About - My Air App")),
            air.Body(
                air.H1("About"),
                air.P(
                    "This application was built with the Air web framework, "
                    "which is powered by FastAPI, Starlette, and Pydantic."
                ),
                air.P(air.A("Back to Home", href="/")),
            ),
        )
```

Notice the `air.A("Back to Home", href="/")` tag — this creates an HTML anchor
element `<a href="/">Back to Home</a>`. The `air.A` tag takes the link text as
a positional argument and the `href` URL as a keyword argument.

{{< note >}}
If a function name contains underscores, `@app.page` converts them to dashes
in the URL. For example, a function named `contact_us` would create the route
`/contact-us`.
{{< /note >}}

## A Dynamic Greeting Page

Add a route that uses a **path parameter** to generate personalized pages.
Declare the parameter with curly braces in the route path and accept it as a
function argument with a type annotation.

```editor:append-lines-to-file
file: ~/exercises/app.py
text: |4


    @app.get("/greet/{name}")
    async def greet(name: str):
        return air.Html(
            air.Head(air.Title(f"Hello {name}")),
            air.Body(
                air.H1(f"Hello, {name}!"),
                air.P("This page was generated using a path parameter."),
                air.P(air.A("Back to Home", href="/")),
            ),
        )
```

The `{name}` in the route path becomes a variable that Air passes to the
function. The `str` type annotation tells Air to expect a string value. You can
use the parameter directly in Air Tags with Python f-strings.

## Adding Navigation

Now add navigation links to the home page so users can reach the new routes.
Insert a navigation bar after the subtitle:

```editor:append-lines-after-match
file: ~/exercises/app.py
match: "A web application built with Air Tags."
text: |2
              air.P(
                  air.A("Home", href="/"), " | ",
                  air.A("About", href="/about"), " | ",
                  air.A("Greet", href="/greet/World"),
              ),
```

This `air.P` tag mixes `air.A` link tags with plain strings (`" | "`) as
positional arguments. Air Tags render them in order, so the result is links
separated by pipes.

## Testing the Routes

The development server has auto-reloaded with all the changes. Open the
application to see the navigation links:

```dashboard:reload-dashboard
name: App
```

Click the **About** and **Greet** links to navigate between pages. Each page is
a complete HTML document generated from Air Tags.

You can also test the greeting route with different names using the second
terminal:

```terminal:execute
command: |-
  curl -s localhost:8000/greet/Python
session: 2
```

The response is the raw HTML that Air generated from the Air Tags in the
`greet` function. Try changing `Python` in the URL to any name to see the path
parameter in action:

```terminal:execute
command: |-
  curl -s localhost:8000/greet/Educates
session: 2
```
