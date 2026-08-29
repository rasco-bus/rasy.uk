from js import Response, URL

async def on_fetch(request, env):
    # 1. Check what the browser is trying to load
    req_url = URL.new(request.url)
    
    # 2. If it is automatically looking for the favicon, send it to your GitHub image
    if req_url.pathname == "/favicon.ico":
        return Response.redirect("https://raw.githubusercontent.com/rasco-bus/rasy.uk/main/images/tabicon.png", 301)

    # 3. Otherwise, load the normal HTML website
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Coming Soon</title>
        <link rel="icon" href="https://raw.githubusercontent.com/rasco-bus/rasy.uk/main/images/tabicon.png" type="image/png">
        <style>
            body { 
                display: flex; 
                flex-direction: column;
                justify-content: center; 
                align-items: center; 
                height: 100vh; 
                margin: 0; 
                font-family: 'Courier New', Courier, monospace; 
                background-color: #1a1a1a; 
                color: white;
                position: relative; /* Added to keep absolute positioning relative to the body */
            }
            .logo {
                position: absolute;
                top: 20px;
                left: 20px;
                width: 150px; /* Adjust this value to make your logo bigger or smaller */
                height: auto;
            }
            h1 { 
                font-size: 5rem; 
                margin-bottom: 10px;
            }
            p {
                font-size: 1.5rem;
                color: #a0a0a0;
            }
        </style>
    </head>
    <body>
        <!-- Added the logo image here -->
        <img src="https://raw.githubusercontent.com/rasco-bus/rasy.uk/main/images/toplefticon.png" alt="Logo" class="logo">
        
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
