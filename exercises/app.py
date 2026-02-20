import air

app = air.Air()


@app.get("/")
async def index():
    return air.Html(
        air.Head(air.Title("My Air App")),
        air.Body(
            air.H1("Hello, World!"),
            air.P("Welcome to the Air web framework."),
        ),
    )
