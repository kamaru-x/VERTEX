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
        <?php include ('header.php'); ?>
      
     <style>
            .box{
                box-shadow: none;
            }
        </style>
      
      <!-- BEGIN: Content -->
        <div class="content">

            <h2 class="intro-y text-lg font-medium mt-10" style="text-align: center;font-size: 35px;color:#1e40af;padding-top: 30px;padding-bottom: 30px;border-bottom: solid 1px #bcbcbc;">Proposal Wise Report</h2>

            <div class="grid grid-cols-12 gap-6">
                <div class="col-span-12 2xl:col-span-12">
                    <div class="grid grid-cols-12 gap-6">
                      
                        <!-- BEGIN: Sales Report -->
                        <div class="col-span-12 lg:col-span-12 mt-8">
                            <div class="intro-y block sm:flex items-center h-10">
                                <h2 class="text-lg font-medium truncate mr-5">
                                    Sum Of Total Target
                                </h2>
                                <div class="sm:ml-auto mt-3 sm:mt-0 relative text-slate-500">
                                    <!-- <i data-lucide="calendar" class="w-4 h-4 z-10 absolute my-auto inset-y-0 ml-3 left-0"></i> 
                                    <input type="text" class="datepicker form-control sm:w-56 box pl-10"> -->
                                </div>
                            </div>
                            <div class="intro-y box p-5 mt-12 sm:mt-5">
                                <div class="flex flex-col md:flex-row md:items-center">
                                    <div class="flex">
                                        <div>
                                            <div class="text-primary dark:text-slate-300 text-lg xl:text-xl font-medium">345,000</div>
                                            <div class="mt-0.5 text-slate-500">Target Given</div>
                                        </div>
                                        <div class="w-px h-12 border border-r border-dashed border-slate-200 dark:border-darkmode-300 mx-4 xl:mx-5"></div>
                                        <div>
                                            <div class="text-slate-500 text-lg xl:text-xl font-medium">134,000</div>
                                            <div class="mt-0.5 text-slate-500">Achieved</div>
                                        </div>
                                         <div class="w-px h-12 border border-r border-dashed border-slate-200 dark:border-darkmode-300 mx-4 xl:mx-5"></div>
                                        <div>
                                            <div class="text-slate-500 text-lg xl:text-xl font-medium text-warning">233,000</div>
                                            <div class="mt-0.5 text-slate-500">Failed</div>
                                        </div>
                                    </div>
                                    <div class="dropdown md:ml-auto mt-5 md:mt-0">
                                        <!-- <button class="dropdown-toggle btn btn-outline-secondary font-normal" aria-expanded="false" data-tw-toggle="dropdown"> Filter by Category <i data-lucide="chevron-down" class="w-4 h-4 ml-2"></i> </button>
                                        <div class="dropdown-menu w-40">
                                            <ul class="dropdown-content overflow-y-auto h-32">
                                                <li><a href="" class="dropdown-item">PC & Laptop</a></li>
                                                <li><a href="" class="dropdown-item">Smartphone</a></li>
                                                <li><a href="" class="dropdown-item">Electronic</a></li>
                                                <li><a href="" class="dropdown-item">Photography</a></li>
                                                <li><a href="" class="dropdown-item">Sport</a></li>
                                            </ul>
                                        </div> -->
                                    </div>
                                </div>
                                <a href="report-proposal-total.php"><div class="report-chart">
                                    <div class="h-[275px]">
                                        <canvas id="report-line-chart" class="mt-6 -mb-6"></canvas>
                                    </div>
                                </div></a>
                            </div>
                        </div>
                        <!-- END: Sales Report -->
                        
                         
                        
                        
                    </div>
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