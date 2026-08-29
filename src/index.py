from js import Response, URL

async def on_fetch(request, env):
    req_url = URL.new(request.url)
    
    # 1. Favicon route
    if req_url.pathname == "/favicon.ico":
        return Response.redirect("https://raw.githubusercontent.com/rasco-bus/rasy.uk/main/images/tabicon.png", 301)
        
    # 2. Robots.txt route (NEW)
    elif req_url.pathname == "/robots.txt":
        # This tells all search engines (*) they are allowed to crawl your entire site (/)
        robots_content = "User-agent: *\nAllow: /\n"
        
        res = Response.new(robots_content)
        res.headers.set("Content-Type", "text/plain")
        return res

    # 3. Default route for your website
    else:
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Coming Soon</title>
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
        
        res = Response.new(html)
        res.headers.set("Content-Type", "text/html")
        return res
