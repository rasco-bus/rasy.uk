from js import Response, URL

# 1. Define static content at the module level so it's only created once
ROBOTS_CONTENT = "User-agent: *\nAllow: /\n"

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Rasy UK</title>
    <meta name="description" content="Official website for Rasy UK. Currently under construction. Contact us for inquiries." />
    <meta name="google-site-verification" content="bJuODXWAuViJT6d-FQSEnBpYx_e4-nNJVrlkKnHyd3s" />
    
    <!-- FIX: Added Canonical Tag -->
    <link rel="canonical" href="https://rasy.uk/" />
    
    <!-- Open Graph Tags -->
    <meta property="og:title" content="Rasy UK" />
    <meta property="og:description" content="Our new website is under construction. Contact us today." />
    <meta property="og:image" content="https://raw.githubusercontent.com/rasco-bus/rasy.uk/main/images/toplefticon.png" />
    
    <link rel="icon" href="https://raw.githubusercontent.com/rasco-bus/rasy.uk/main/images/tabicon.png" type="image/png">
    <style>
        body { 
            display: flex; 
            flex-direction: column;
            justify-content: center; 
            align-items: center; 
            min-height: 100vh; 
            margin: 0; 
            font-family: 'Courier New', Courier, monospace; 
            color: white;
            position: relative;
            text-align: center;

            /* Sky Blue & Grey animated gradient */
            background: linear-gradient(-45deg, #1f2937, #3b82f6, #374151, #60a5fa);
            background-size: 400% 400%;
            animation: gradientShift 14s ease infinite;
        }

        /* Animation keyframes for the smooth moving effect */
        @keyframes gradientShift {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
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
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        }
        p { 
            font-size: 1.5rem; 
            color: #f3f4f6; 
            margin: 10px 0; 
            text-shadow: 0 1px 6px rgba(0, 0, 0, 0.3);
        }
        a.contact { 
            color: #ffffff; 
            font-weight: bold;
            text-decoration: underline; 
        }
        a.contact:hover { 
            color: #d1d5db; 
        }
    </style>
</head>
<body>
    <a href="/" class="logo-link">
        <img src="https://raw.githubusercontent.com/rasco-bus/rasy.uk/main/images/toplefticon.png" alt="Rasy UK Company Logo" class="logo">
    </a>
    
    <h1>COMING SOON</h1>
    <p>Our new website is under construction.</p>
    <p>Please call <a href="tel:+447842581975" class="contact">07842 581975</a></p>
    <p>or email <a href="mailto:contact@rasy.uk" class="contact">contact@rasy.uk</a>.</p>
</body>
</html>
"""

async def on_fetch(request, env):
    req_url = URL.new(request.url)
    
    # Evaluate the path once
    path = req_url.pathname
    
    # 2. Favicon route
    if path == "/favicon.ico":
        res = Response.redirect("https://raw.githubusercontent.com/rasco-bus/rasy.uk/main/images/tabicon.png", 301)
        res.headers.set("Cache-Control", "public, max-age=86400")
        return res
        
    # 3. Robots.txt route
    if path == "/robots.txt":
        res = Response.new(ROBOTS_CONTENT)
        res.headers.set("Content-Type", "text/plain")
        res.headers.set("Cache-Control", "public, max-age=86400")
        return res

    # FIX: Redirect any random URL paths to the homepage to prevent duplicate content
    if path != "/":
        return Response.redirect("https://rasy.uk/", 301)

    # 4. Default route strictly for the root website ("/")
    res = Response.new(HTML_CONTENT)
    res.headers.set("Content-Type", "text/html")
    res.headers.set("X-Frame-Options", "DENY")
    res.headers.set("X-Content-Type-Options", "nosniff")
    
    return res
