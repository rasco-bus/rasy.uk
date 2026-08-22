from workers import WorkerEntrypoint, Response

class Default(WorkerEntrypoint):
    async def fetch(self, request):
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
        
        headers = {"content-type": "text/html;charset=UTF-8"}
        return Response(html, headers=headers)
