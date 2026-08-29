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
        <!-- Google Search Console Verification Tag -->
        <meta name="google-site-verification" content="bJuODXWAuViJT6d-FQSEnBpYx_e4-nNJVrlkKnHyd3s" />
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
                position: relative;
            }
            .logo-link {
                position: absolute;
                top: 20px;
                left: 20px;
            }
            .logo {
                width: 150px; 
                height: auto;
                border: none; 
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
        <a href="/" class="logo-link">
            <img src="https://raw.githubusercontent.com/rasco-bus/rasy.uk/main/images/toplefticon.png" alt="Logo" class="logo">
        </a>
        
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
