from js import Response

async def on_fetch(request, env):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Coming Soon</title>
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
        <h1>COMING SOON</h1>
        <p>Our new website is under construction.</p>
    </body>
    </html>
    """
    
    # Safely create the response first
    res = Response.new(html)
    # Safely add the HTML header on a separate line to prevent Pyodide from crashing
    res.headers.set("Content-Type", "text/html")
    
    return res
