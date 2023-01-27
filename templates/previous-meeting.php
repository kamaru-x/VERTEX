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
        <title>Vertex Engineering WLL</title>
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
            @media(max-width: 575px)
            {
                .intro-y .box {
                    width: 100%!important;
                }
            }
            
        </style>
        <?php include ('header.php'); ?>
        <!-- BEGIN: Content -->
    <div class="content">
            <div class="flex items-center mt-8">
        <!-- <h2 class="intro-y text-lg font-medium mr-auto"></h2> -->
    </div>
    <!-- BEGIN: Wizard Layout -->
    <div class="intro-y box py-10 sm:py-20 mt-5">
        <h2 style=" font-size: 30px; font-weight: 500; text-align: center;
        color: #1e40af;">Previous Meetings</h2>
        
        <div class="px-5 sm:px-20 mt-10 pt-10 border-t border-slate-200/60 dark:border-darkmode-400">
            <!-- <div class="font-medium text-base">Add / Manage Products</div> -->
                                    <div class="col-span-12">
                
                                        <div class="overflow-x-auto">
                                            <table class="table">
                                                <thead class="table-dark">
                                                    <tr>
                                                        <th class="whitespace-nowrap">Date</th>
                                                        <th class="whitespace-nowrap">Company Name</th>
                                                        <th class="whitespace-nowrap">Salesman</th>
                                                        <th class="whitespace-nowrap">Mode Of Meeting</th>
                                                        <th class="whitespace-nowrap">Time (From)</th>
                                                        <th class="whitespace-nowrap">Time (To)</th>
                                                         <th class="whitespace-nowrap">Description</th>
                                                         <th class="whitespace-nowrap">Remark</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <td>1/12/2023</td>
                                                         <td>ABC International<br>4433 6688 / info@abcdintl.com</td>
                                                        <td>Ramshad Hassan<br>
                                                         ID#12345</td>
                                                        <td>Online</td>
                                                        <td>10:00 AM</td>
                                                        <td>12:00 PM</td>
                                                        <td>Add updates by monday</td>
                                                        <td>Status updated</td>
                                                    </tr>
                                                    <tr>
                                                        <td>1/12/2023</td>
                                                         <td>ABC International<br>4433 6688 / info@abcdintl.com</td>
                                                        <td>Ramshad Hassan<br>
                                                         ID#12345</td>
                                                        <td>Direct</td>
                                                        <td>10:00 AM</td>
                                                        <td>12:00 PM</td>
                                                        <td>Add updates by monday</td>
                                                        <td>Status updated</td>
                                                    </tr>
                                                    <tr>
                                                        <td>1/12/2023</td>
                                                         <td>ABC International<br>4433 6688 / info@abcdintl.com</td>
                                                        <td>Ramshad Hassan<br>
                                                         ID#12345</td>
                                                        <td>Telephone</td>
                                                        <td>10:00 AM</td>
                                                        <td>12:00 PM</td>
                                                        <td>Add updates by monday</td>
                                                        <td>Status updated</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                
            </div>
        </div>
    </div>
    <!-- END: Wizard Layout -->
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