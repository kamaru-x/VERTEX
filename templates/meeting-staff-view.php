
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
<!-- BEGIN: Content -->
        <div class="content">
            <div class="intro-y flex items-center mt-8">
               <!--  <h2 class="text-lg font-medium mr-auto">
                    Profile Layout
                </h2> -->
            </div>
            <!-- BEGIN: Profile Info -->
            <div class="intro-y box px-5 pt-5 mt-5">
                <div class="flex flex-col lg:flex-row border-b border-slate-200/60 dark:border-darkmode-400 pb-5 -mx-5">
                    <div class="flex flex-1 px-5 items-center justify-center lg:justify-start">
                       
                        <div class="">
                            <div class="w-24 sm:w-40 truncate sm:whitespace-normal font-medium text-lg" style=" color: #2b53d8;">Ramshad Hassan</div>
                            <div class="text-slate-500">Salesman</div>
                        </div>
                    </div>
                    <div class="mt-6 lg:mt-0 flex-1 px-5 border-l border-r border-slate-200/60 dark:border-darkmode-400 border-t lg:border-t-0 pt-5 lg:pt-0">
                        <div class="font-medium text-center lg:text-left lg:mt-3">Contact Details</div>
                        <div class="flex flex-col justify-center items-center lg:items-start mt-4">
                             <div class="truncate sm:whitespace-normal flex items-center mt-3 mb-3"> <i data-lucide="phone" class="w-4 h-4 mr-2"></i> 555 3380 </div>
                            <div class="truncate sm:whitespace-normal flex items-center"> <i data-lucide="mail" class="w-4 h-4 mr-2"></i> ramshad@vertex.com.qa </div>
                           
                        </div>
                    </div>
                    <div class="mt-6 lg:mt-0 flex-1 px-5 border-t lg:border-0 border-slate-200/60 dark:border-darkmode-400 pt-5 lg:pt-0">
                        <div class="font-medium text-center lg:text-left lg:mt-5">Sales Growth</div>
                        <div class="flex items-center justify-center lg:justify-start mt-2">
                            <div class="mr-2 w-20 flex"> USP: <span class="ml-3 font-medium text-success">+23%</span> </div>
                            <div class="w-3/4">
                                <div class="h-[55px]">
                                    <canvas class="simple-line-chart-1 -mr-5"></canvas>
                                </div>
                            </div>
                        </div>
                        <div class="flex items-center justify-center lg:justify-start">
                            <div class="mr-2 w-20 flex"> STP: <span class="ml-3 font-medium text-danger">-2%</span> </div>
                            <div class="w-3/4">
                                <div class="h-[55px]">
                                    <canvas class="simple-line-chart-2 -mr-5"></canvas>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
               
            </div>
            <!-- END: Profile Info -->
             <!-- BEGIN: Data List -->
        <div class="intro-y col-span-12 overflow-auto 2xl:overflow-visible">
            <h2 class="intro-y text-lg font-medium mt-10" style="text-align: center;font-size: 35px;color:#1e40af;padding-top: 30px;padding-bottom: 30px;border-bottom: solid 1px #bcbcbc;">Upcoming Meetings</h2>
            <table class="table table-report -mt-2">
                <thead>
                    <tr>
                        <th class="whitespace-nowrap" style="text-align: center;">DATE</th>
                        <th class="whitespace-nowrap">COMPANY NAME</th>
                        <th class="whitespace-nowrap">REFERENCE (LEAD REFERENCE)</th>
                         <th class="whitespace-nowrap" >MODE OF MEETING</th>
                         <th class="whitespace-nowrap" style="text-align: left;">TIME</th>
                        <th class="whitespace-nowrap"style="text-align: center;"> DESCRIPTION</th>
                       
                        
                    </tr>
                </thead>
                <tbody>
                        <tr class="intro-x">
                            <td class="w-40 ref">
                                <div class="font-medium whitespace-nowrap">23/10/2023</div>   
                            </td>
                            <td class="w-60 text-primary">
                                <a href="meeting-staff-upcoming.php " class="font-medium whitespace-nowrap">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                </div>
                            </td>
                            <td class="w-60 ref">
                                <div class="font-medium whitespace-nowrap">REF:12345</div>   
                            </td>
                            <td class="w-60 text-left">
                                <div class="pr-16">Online</div>
                            </td>
                            <td class="w-60 text-center">
                                <div class="pr-16">10.00AM-12.00PM</div>
                            </td>

                             <td class="w-60 text-right">
                                <div class="pr-16">Description Here</div>
                            </td>
                             
                        </tr>

                        <tr class="intro-x">
                            <td class="w-40 ref">
                                <div class="font-medium whitespace-nowrap">23/10/2023</div>   
                            </td>
                            <td class="w-60 text-primary">
                                <a href="meeting-staff-upcoming.php" class="font-medium whitespace-nowrap">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                </div>
                            </td>
                            <td class="w-60 ref">
                                <div class="font-medium whitespace-nowrap">REF:12345</div>   
                            </td>
                            <td class="w-60 text-left">
                                <div class="pr-16">Online</div>
                            </td>
                            <td class="w-60 text-center">
                                <div class="pr-16">10.00AM-12.00PM</div>
                            </td>

                            <td class="w-60 text-right">
                                <div class="pr-16">Description Here</div>
                            </td>
                             <!-- <td class="table-report__action">
                                <div class="flex justify-center items-center">
                                   

                                    <a class="flex items-center text-primary whitespace-nowrap mr-5" href="meeting-staff-upcoming.php">
                                        <i data-lucide="eye" class="w-4 h-4 mr-1"></i> 
                                    </a>
                                  
                                </div>
                            </td> -->
                        </tr>

                        <tr class="intro-x">
                            <td class="w-40 ref">
                                <div class="font-medium whitespace-nowrap">23/10/2023</div>   
                            </td>
                            <td class="w-60 text-primary">
                                <a href="meeting-staff-upcoming.php" class="font-medium whitespace-nowrap">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                </div>
                            </td>
                            <td class="w-60 ref">
                                <div class="font-medium whitespace-nowrap">REF:12345</div>   
                            </td>
                            <td class="w-60 text-left">
                                <div class="pr-16">Online</div>
                            </td>
                            <td class="w-60 text-center">
                                <div class="pr-16">10.00AM-12.00PM</div>
                            </td>

                             <td class="w-60 text-right">
                                <div class="pr-16">Description Here</div>
                            </td>
                            
                        </tr>


                        <tr class="intro-x">
                           <td class="w-40 ref">
                                <div class="font-medium whitespace-nowrap">23/10/2023</div>   
                            </td>
                            <td class="w-60 text-primary">
                                <a href="meeting-staff-upcoming.php" class="font-medium whitespace-nowrap">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                </div>
                            </td>
                            <td class="w-60 ref">
                                <div class="font-medium whitespace-nowrap">REF:12345</div>   
                            </td>
                            <td class="w-60 text-left">
                                <div class="pr-16">Online</div>
                            </td>
                            <td class="w-60 text-center">
                                <div class="pr-16">10.00AM-12.00PM</div>
                            </td>

                             <td class="w-60 text-right">
                                <div class="pr-16">Description Here</div>
                            </td>
                            
                        </tr>

         
                    </tbody>
            </table>
        </div>
        <!-- END: Data List -->

             <!-- BEGIN: Data List -->
        <div class="intro-y col-span-12 overflow-auto 2xl:overflow-visible">
            <h2 class="intro-y text-lg font-medium mt-10" style="text-align: center;font-size: 35px;color:#1e40af;padding-top: 30px;padding-bottom: 30px;border-bottom: solid 1px #bcbcbc;">Previous Meetings</h2>
            <table class="table table-report -mt-2">
                <thead>
                    <tr>
                        <th class="whitespace-nowrap" style="text-align: center;">DATE</th>
                        <th class="whitespace-nowrap">COMPANY NAME</th>
                        <th class="whitespace-nowrap">REFERENCE (LEAD REFERENCE)</th>
                         <th class="whitespace-nowrap" >MODE OF MEETING</th>
                         <th class="whitespace-nowrap" style="text-align: left;">TIME</th>
                        <th class="whitespace-nowrap"style="text-align: center;"> DESCRIPTION</th>
                         <th class="whitespace-nowrap"style="text-align: center;"> ACTION</th>
                        
                        
                    </tr>
                </thead>
                <tbody>
                        <tr class="intro-x">
                           <td class="w-40 ref">
                                <div class="font-medium whitespace-nowrap">23/10/2023</div>   
                            </td>
                            <td class="w-60 text-primary">
                                <a href="meeting-staff-previous.php" class="font-medium whitespace-nowrap">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                </div>
                            </td>
                            <td class="w-60 ref">
                                <div class="font-medium whitespace-nowrap">REF:12345</div>   
                            </td>
                            <td class="w-60 text-left">
                                <div class="pr-16">Online</div>
                            </td>
                            <td class="w-60 text-center">
                                <div class="pr-16">10.00AM - 12.00PM</div>
                            </td>

                             <td class="w-60 text-right">
                                <div class="pr-16">Description Here</div>
                            </td>
                             <td class="table-report__action">
                                <div class="flex justify-center items-center">
                                   

                                    <a class="flex items-center text-primary whitespace-nowrap mr-5" href="meeting-staff-previous.php">
                                        <i data-lucide="eye" class="w-4 h-4 mr-1"></i> 
                                    </a>
                                  
                                </div>
                            </td>
                        </tr>

                        <tr class="intro-x">
                           <td class="w-40 ref">
                                <div class="font-medium whitespace-nowrap">23/10/2023</div>   
                            </td>
                            <td class="w-60 text-primary">
                                <a href="meeting-staff-previous.php" class="font-medium whitespace-nowrap">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                </div>
                            </td>
                            <td class="w-60 ref">
                                <div class="font-medium whitespace-nowrap">REF:12345</div>   
                            </td>
                            <td class="w-60 text-left">
                                <div class="pr-16">Online</div>
                            </td>
                            <td class="w-60 text-center">
                                <div class="pr-16">10.00AM - 12.00PM</div>
                            </td>

                             <td class="w-60 text-right">
                                <div class="pr-16">Description Here</div>
                            </td>
                             <td class="table-report__action">
                                <div class="flex justify-center items-center">
                                   

                                    <a class="flex items-center text-primary whitespace-nowrap mr-5" href="meeting-staff-previous.php">
                                        <i data-lucide="eye" class="w-4 h-4 mr-1"></i> 
                                    </a>
                                  
                                </div>
                            </td>
                        </tr>

                        <tr class="intro-x">
                           <td class="w-40 ref">
                                <div class="font-medium whitespace-nowrap">23/10/2023</div>   
                            </td>
                            <td class="w-60 text-primary">
                                <a href="meeting-staff-details.php" class="font-medium whitespace-nowrap">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                </div>
                            </td>
                            <td class="w-60 ref">
                                <div class="font-medium whitespace-nowrap">REF:12345</div>   
                            </td>
                            <td class="w-60 text-left">
                                <div class="pr-16">Online</div>
                            </td>
                            <td class="w-60 text-center">
                                <div class="pr-16">10.00AM - 12.00PM</div>
                            </td>

                            <td class="w-60 text-right">
                                <div class="pr-16">Description Here</div>
                            </td>
                             <td class="table-report__action">
                                <div class="flex justify-center items-center">
                                   

                                    <a class="flex items-center text-primary whitespace-nowrap mr-5" href="meeting-staff-previous.php">
                                        <i data-lucide="eye" class="w-4 h-4 mr-1"></i> 
                                    </a>
                                  
                                </div>
                            </td>
                        </tr>


                        <tr class="intro-x">
                           <td class="w-40 ref">
                                <div class="font-medium whitespace-nowrap">23/10/2023</div>   
                            </td>
                            <td class="w-60 text-primary">
                                <a href="meeting-staff-previous.php" class="font-medium whitespace-nowrap">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                </div>
                            </td>
                            <td class="w-60 ref">
                                <div class="font-medium whitespace-nowrap">REF:12345</div>   
                            </td>
                            <td class="w-60 text-left">
                                <div class="pr-16">Online</div>
                            </td>
                            <td class="w-60 text-center">
                                <div class="pr-16">10.00AM - 12.00PM</div>
                            </td>

                            <td class="w-60 text-right">
                                <div class="pr-16">Description Here</div>
                            </td>
                             <td class="table-report__action">
                                <div class="flex justify-center items-center">
                                   

                                    <a class="flex items-center text-primary whitespace-nowrap mr-5" href="meeting-staff-previous.php">
                                        <i data-lucide="eye" class="w-4 h-4 mr-1"></i> 
                                    </a>
                                  
                                </div>
                            </td>
                        </tr>

         
                    </tbody>
            </table>
        </div>
        <!-- END: Data List -->
           
        <!-- END: Content -->
        <style>
        .dark-mode-switcher{
            display: none;
        }
        .ref{
            text-align: center!important;
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