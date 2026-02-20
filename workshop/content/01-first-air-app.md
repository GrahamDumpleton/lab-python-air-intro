---
title: Your First Air App
---

A starter Air application is ready for you in `app.py`. Open it in the editor
to see how it works.

```editor:open-file
file: ~/exercises/app.py
```

The application has three key parts:

- **`air.Air()`** creates the application instance, similar to `FastAPI()` or
  `Flask(__name__)` in other frameworks.

- **`@app.get("/")`** defines a route that handles GET requests to the root
  URL. This decorator works exactly like FastAPI's `@app.get()`.

- **Air Tags** like `air.Html`, `air.Head`, `air.Body`, `air.H1`, and `air.P`
  compose the HTML response. Each tag is a Python class that renders to its
  corresponding HTML element.

Each Air Tag accepts **positional arguments** as child content (text or nested
tags) and **keyword arguments** as HTML attributes. For example,
`air.H1("Hello, World!")` renders to `<h1>Hello, World!</h1>`.

## Running the Application

Start the Air development server in the first terminal:

```terminal:execute
command: air run app
```

The server starts on port 8000 with auto-reload enabled — it will
automatically pick up file changes without needing a restart.

Open the application in the dashboard:

```dashboard:open-dashboard
name: App
```

You should see a page with a heading and a welcome paragraph — the HTML
generated from the Air Tags in your `index` function.
