import SOAPpy
server = SOAPpy.SOAPProxy("http://localhost:8080/")
server.app.run()