from js import Response, URL

async def on_fetch(request, env):
    # Check for the favicon background request
    req_url = URL.new(request.url)
    if req_url.pathname == "/favicon.ico":
        return Response.redirect("https://raw.githubusercontent.com/rasco-bus/rasy.uk/main/images/tabicon.png", 301)

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Coming Soon</title>
        <!-- Your Favicon -->
        <link rel="icon" href="https://raw.githubusercontent.com/rasco-bus/rasy.uk/main/images/tabicon.png" type="image/png">
        
        <!-- Import the Google Fonts (Inter and Montserrat) -->
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Inter&family=Montserrat:wght@800&display=swap" rel="stylesheet">
        
        <style>
            body { 
                display: flex; 
                flex-direction: column;
                justify-content: center; 
                align-items: center; 
                height: 100vh; 
                margin: 0; 
                /* Apply the 'Inter' font to the main body */
                font-family: 'Inter', sans-serif; 
                background-color: #1a1a1a; 
                color: white;
            }
            h1 { 
                /* Apply the 'Montserrat' font to the big header */
                font-family: 'Montserrat', sans-serif;
                font-size: 5rem; 
                margin-bottom: 10px;
                letter-spacing: -2px;
            }
            p {
                font-size: 1.5rem;
                color: #a0a0a0;
            }
        </style>
    </head>
    <body>
        <h1>COMING SOON</h1>
        <p>Our new website is under construction.</p>
        <p>Please call 07842 581975.</p>
    </body>
    </html>
    """
    
    # Safely create the response first
    res = Response.new(html)
    # Safely add the HTML header on a separate line to prevent Pyodide from crashing
    res.headers.set("Content-Type", "text/html")
    
    return res
