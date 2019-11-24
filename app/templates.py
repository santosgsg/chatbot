class Template:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
    def getAtividades(self):
        return f'''<!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Table V03</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
        <!--===============================================================================================-->	
            <link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="css/util.css">
            <link rel="stylesheet" type="text/css" href="css/main.css">
        <!--===============================================================================================-->
        </head>
        <body>
            
            <div class="limiter">
                <div class="container-table100">
                    <div class="wrap-table100">				
        
                        <div class="table100 ver5 m-b-110">
                            <table data-vertable="ver5">
                                <thead>
                                    {{ columns }}
                                </thead>
                                <tbody>
                                     {{rows}}
                                </tbody>
                            </table>
                        </div>
                        
                    </div>
                </div>
            </div>
        
        
            
        
        <!--===============================================================================================-->	
            <script src="vendor/jquery/jquery-3.2.1.min.js"></script>
        <!--===============================================================================================-->
            <script src="vendor/bootstrap/js/popper.js"></script>
            <script src="vendor/bootstrap/js/bootstrap.min.js"></script>
        <!--===============================================================================================-->
            <script src="vendor/select2/select2.min.js"></script>
        <!--===============================================================================================-->
            <script src="js/main.js"></script>
        
        </body>
        </html>'''