<!DOCTYPE html>

<html lang="en" class="light">
    <!-- BEGIN: Head -->
    <head>
        <meta charset="utf-8">
        <link href="dist/images/logo.png" rel="shortcut icon">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="Vertex Engineering LLC">
        <meta name="keywords" content="Vertex Engineering LLC">
        <meta name="author" content="Vertex Engineering LLC">
        <title>Vertex Engineering LLC</title>
        <!-- BEGIN: CSS Assets-->
        <link rel="stylesheet" href="dist/css/app.css" />
        <!-- END: CSS Assets-->
    </head>
    <!-- END: Head -->
    <body class="py-5">
         <style>
            .form-control {
                margin-bottom: 14px;
            }
        </style>
        <?php include ('header.php'); ?> 
  <!-- BEGIN: Content -->
        <div class="content">
            <div class="intro-y items-center mt-8">
                <h2 style="text-align: center;font-size: 30px;color:#1e40af;padding-top: 30px;padding-bottom: 30px;">Change Password</h2>
            </div>
            <div class=" items-center" style="margin-right:auto; margin-left: auto; display: block;">
                <!-- BEGIN: Profile Menu -->
               
                <!-- END: Profile Menu -->
                <div class="col-span-12 lg:col-span-12 2xl:col-span-12"  >
                    <!-- BEGIN: Change Password -->
                    <div class="intro-y box lg:mt-5" >
                        
                        <div class="p-5" >
                            <div class="col-md-6 col-sm-6 col-xs-12 col-12">
                                <label for="change-password-form-1" class="form-label">Old Password <span style="color:red;">*</span></label>
                                <input id="change-password-form-1" type="password" class="form-control" placeholder="Input text">
                            </div>
                            <div class="col-md-6 col-sm-6 col-xs-12 col-12 mt-3">
                                <label for="change-password-form-2" class="form-label">New Password <span style="color:red;">*</span></label>
                                <input id="change-password-form-2" type="password" class="form-control" placeholder="Input text">
                            </div>
                            <div class="col-md-6 col-sm-6 col-xs-12 col-12 mt-3">
                                <label for="change-password-form-3" class="form-label">Confirm New Password <span style="color:red;">*</span></label>
                                <input id="change-password-form-3" type="password" class="form-control" placeholder="Input text">
                            </div>
                            <button type="button" class="btn btn-primary mt-4">Change Password</button>
                        </div>
                    </div>
                    <!-- END: Change Password -->
                </div>
            </div>
        </div>
        <!-- END: Content -->
        <style>
        .dark-mode-switcher{
            display: none;
        }
        
    </style>
        <!-- BEGIN: Dark Mode Switcher-->
        <div data-url="top-menu-dark-regular-form.html" class="dark-mode-switcher cursor-pointer shadow-md fixed bottom-0 right-0 box border rounded-full w-40 h-12 flex items-center justify-center z-50 mb-10 mr-10">
            <div class="mr-4 text-slate-600 dark:text-slate-200">Dark Mode</div>
            <div class="dark-mode-switcher__toggle border"></div>
        </div>
        <!-- END: Dark Mode Switcher-->
        
        <!-- BEGIN: JS Assets-->
        <script src="https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/markerclusterer.js"></script>
        <script src="https://maps.googleapis.com/maps/api/js?key=["your-google-map-api"]&libraries=places"></script>
        <script src="dist/js/app.js"></script>
        <!-- END: JS Assets-->
    </body>
</html>