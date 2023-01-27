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

               <h2 class="intro-y text-lg font-medium mt-10" style="text-align: center;font-size: 35px;color:#1e40af;padding-top: 30px;padding-bottom: 30px;border-bottom: solid 1px #bcbcbc;">Pending Task</h2>
         <!--   <div class="intro-y box py-10 sm:py-20 mt-5">
        <h2 style=" font-size: 30px; font-weight: 500; text-align: center;
        color: #1e40af;">Add Category</h2>
    </div> -->
    <div class="grid grid-cols-12 gap-6 mt-5">
        <div class="intro-y col-span-12 flex flex-wrap xl:flex-nowrap items-center mt-2">
            
            <div class="hidden xl:block mx-auto text-slate-500"></div>
            <div class="w-full xl:w-auto flex items-center mt-3 xl:mt-0">
               
               
                <a href="create-task.php"><button class="btn btn-primary shadow-md mr-2">Create Task</button></a>
                
            
            </div>
        </div>
        <!-- BEGIN: Data List -->
        <div class="intro-y col-span-12 overflow-auto 2xl:overflow-visible">
            <table class="table table-report -mt-2">
                <thead>
                    <tr>
                        
                        <th class="whitespace-nowrap">COMPANY NAME</th>
                        <th class="whitespace-nowrap">REFERENCE (LEAD REFERENCE)</th>
                       
                        <th class="whitespace-nowrap">
                            <div class="pr-16">SALESMAN</div>
                        </th>
                         <th class="whitespace-nowrap" >TASK TITLE</th>
                         
                        <th class="whitespace-nowrap"style="text-align: left;"> PRIORITY </th>
                        <th class="whitespace-nowrap mob" > DUE DATE </th>
                        <th class="text-center whitespace-nowrap">ACTIONS</th>
                    </tr>
                </thead>
                <tbody>
                        <tr class="intro-x">
                            
                            <td class="w-60">
                                <a href="" class="font-medium whitespace-nowrap text-primary">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                </div>
                            </td>
                            <td class="w-60 ref">
                                <a href="" class="font-medium whitespace-nowrap">REF:12345</a>
                                 
                            </td>
                           
                           <td class="w-60">
                                <a href="" class="font-medium whitespace-nowrap text-primary">Ramshad Hassan</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">5500 3488</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">ramshad@vertex.com.qa</div>
                            </td>
                            <td class="w-60 text-center">
                                <div class="pr-16">Inventory Procurement</div>
                            </td>
                            

                            <td class="w-40 text-danger">
                                <div class="pr-16">High</div>
                            </td>

                             <td class="text-center">
                                <div class="flex items-center justify-center whitespace-nowrap text-danger">
                                     2/10/2023
                                </div>
                            </td>
                            
                            <td class="table-report__action">
                                <div class="flex justify-center items-center">
                                    <a class="flex items-center text-primary whitespace-nowrap" href="task-edit.php" data-tw-toggle="modal" data-tw-target="#delete-confirmation-modal">
                                        <i data-lucide="edit" class="w-4 h-4 mr-1"></i>
                                    </a> &nbsp &nbsp

                                    <a class="flex items-center text-primary whitespace-nowrap mr-5" href="view-task-pending.php">
                                        <i data-lucide="eye" class="w-4 h-4 mr-1"></i> 
                                    </a>
                                    <a class="flex items-center text-success whitespace-nowrap mr-5" href="#" data-tw-toggle="modal" data-tw-target="#new-order-modal2" title="Mark As Completed">
                                        <i data-lucide="check-square" class="w-4 h-4 mr-2"></i> 
                                    </a>
                                    
                                  
                                </div>
                            </td>
                        </tr>

                        <tr class="intro-x">
                            
                            <td class="w-60">
                                <a href="" class="font-medium whitespace-nowrap text-primary">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                </div>
                            </td>
                            <td class="w-60 ref">
                                <a href="" class="font-medium whitespace-nowrap">REF:12345</a>
                                 
                            </td>
                           
                           <td class="w-60">
                                <a href="" class="font-medium whitespace-nowrap text-primary">Ramshad Hassan</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">5500 3488</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">ramshad@vertex.com.qa</div>
                            </td>
                            <td class="w-60 text-center">
                                <div class="pr-16">Inventory Procurement</div>
                            </td>
                           
                            <td class="w-40  text-danger">
                                <div class="pr-16">High</div>
                            </td>

                             <td class="text-center">
                                <div class="flex items-center justify-center whitespace-nowrap text-danger">
                                     2/10/2023
                                </div>
                            </td>
                            
                            <td class="table-report__action">
                                <div class="flex justify-center items-center">
                                    <a class="flex items-center text-primary whitespace-nowrap" href="task-edit.php" data-tw-toggle="modal" data-tw-target="#delete-confirmation-modal">
                                        <i data-lucide="edit" class="w-4 h-4 mr-1"></i>
                                    </a> &nbsp &nbsp

                                    <a class="flex items-center text-primary whitespace-nowrap mr-5" href="view-task-pending.php">
                                        <i data-lucide="eye" class="w-4 h-4 mr-1"></i> 
                                    </a>
                                    <a class="flex items-center text-success whitespace-nowrap mr-5" data-tw-toggle="modal" data-tw-target="#new-order-modal2"  href="#" title="Mark As Completed">
                                        <i data-lucide="check-square" class="w-4 h-4 mr-2"></i> 
                                    </a>
                                  
                                </div>
                            </td>
                        </tr>

                        <tr class="intro-x">
                            
                            <td class="w-60">
                                <a href="" class="font-medium whitespace-nowrap text-primary">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                </div>
                            </td>
                            <td class="w-60 ref">
                                <a href="" class="font-medium whitespace-nowrap">REF:12345</a>
                                 
                            </td>
                           
                           <td class="w-60">
                                <a href="" class="font-medium whitespace-nowrap text-primary">Ramshad Hassan</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">5500 3488</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">ramshad@vertex.com.qa</div>
                            </td>
                            <td class="w-60 text-center">
                                <div class="pr-16">Inventory Procurement</div>
                            </td>
                            

                            <td class="w-40  text-success">
                                <div class="pr-16">Normal</div>
                            </td>

                             <td class="text-center">
                                <div class="flex items-center justify-center whitespace-nowrap text-danger">
                                     2/10/2023
                                </div>
                            </td>
                            
                            <td class="table-report__action">
                                <div class="flex justify-center items-center">
                                    <a class="flex items-center text-primary whitespace-nowrap" href="task-edit.php" data-tw-toggle="modal" data-tw-target="#delete-confirmation-modal">
                                        <i data-lucide="edit" class="w-4 h-4 mr-1"></i>
                                    </a> &nbsp &nbsp

                                    <a class="flex items-center text-primary whitespace-nowrap mr-5" href="view-task-pending.php">
                                        <i data-lucide="eye" class="w-4 h-4 mr-1"></i> 
                                    </a>
                                    <a class="flex items-center text-success whitespace-nowrap mr-5"  data-tw-toggle="modal" data-tw-target="#new-order-modal2" href="#" title="Mark As Completed">
                                        <i data-lucide="check-square" class="w-4 h-4 mr-2"></i> 
                                    </a>
                                  
                                </div>
                            </td>
                        </tr>


                        <tr class="intro-x">
                            
                            <td class="w-60">
                                <a href="" class="font-medium whitespace-nowrap text-primary">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                </div>
                            </td>
                            <td class="w-60 ref">
                                <a href="" class="font-medium whitespace-nowrap">REF:12345</a>
                                 
                            </td>
                           
                           <td class="w-60">
                                <a href="" class="font-medium whitespace-nowrap text-primary">Ramshad Hassan</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">5500 3488</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">ramshad@vertex.com.qa</div>
                            </td>
                            <td class="w-60 text-center">
                                <div class="pr-16">Inventory Procurement</div>
                            </td>
                           

                            <td class="w-40  text-warning">
                                <div class="pr-16">Medium</div>
                            </td>

                             <td class="text-center">
                                <div class="flex items-center justify-center whitespace-nowrap text-danger">
                                     2/10/2023
                                </div>
                            </td>
                            
                            <td class="table-report__action">
                                <div class="flex justify-center items-center">
                                    <a class="flex items-center text-primary whitespace-nowrap" href="task-edit.php" data-tw-toggle="modal" data-tw-target="#delete-confirmation-modal">
                                        <i data-lucide="edit" class="w-4 h-4 mr-1"></i>
                                    </a> &nbsp &nbsp

                                    <a class="flex items-center text-primary whitespace-nowrap mr-5" href="view-task-pending.php">
                                        <i data-lucide="eye" class="w-4 h-4 mr-1"></i> 
                                    </a>
                                   <a class="flex items-center text-success whitespace-nowrap mr-5" data-tw-toggle="modal" data-tw-target="#new-order-modal2" href="#" title="Mark As Completed">
                                     
                                        <i data-lucide="check-square" class="w-4 h-4 mr-2"></i> 
                                    </a>

                                  
                                </div>
                            </td>
                        </tr>

         
                    </tbody>
            </table>
        </div>
        <!-- END: Data List -->




        <!-- BEGIN: Pagination -->
        <div class="intro-y col-span-12 flex flex-wrap sm:flex-row sm:flex-nowrap items-center">
            <nav class="w-full sm:w-auto sm:mr-auto">
                <ul class="pagination">
                    <li class="page-item">
                        <a class="page-link" href="#">
                            <i class="w-4 h-4" data-lucide="chevrons-left"></i>
                        </a>
                    </li>
                    <li class="page-item">
                        <a class="page-link" href="#">
                            <i class="w-4 h-4" data-lucide="chevron-left"></i>
                        </a>
                    </li>
                    <li class="page-item">
                        <a class="page-link" href="#">...</a>
                    </li>
                    <li class="page-item">
                        <a class="page-link" href="#">1</a>
                    </li>
                    <li class="page-item active">
                        <a class="page-link" href="#">2</a>
                    </li>
                    <li class="page-item">
                        <a class="page-link" href="#">3</a>
                    </li>
                    <li class="page-item">
                        <a class="page-link" href="#">...</a>
                    </li>
                    <li class="page-item">
                        <a class="page-link" href="#">
                            <i class="w-4 h-4" data-lucide="chevron-right"></i>
                        </a>
                    </li>
                    <li class="page-item">
                        <a class="page-link" href="#">
                            <i class="w-4 h-4" data-lucide="chevrons-right"></i>
                        </a>
                    </li>
                </ul>
            </nav>
            <select class="w-20 form-select box mt-3 sm:mt-0">
                <option>10</option>
                <option>25</option>
                <option>35</option>
                <option>50</option>
            </select>
        </div>
        <!-- END: Pagination -->
    </div>
    
    </div>
    <!-- END: Content -->

    <!-- BEGIN: New Order Modal -->
    <div id="new-order-modal2" class="modal" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h2 class="font-medium text-base mr-auto">Add Remarks</h2>
                </div>
                <div class="modal-body grid grid-cols-12 gap-4 gap-y-3">
                    <div class="col-span-12">
                        <label for="pos-form-1" class="form-label">Date</label>
                         <div class="absolute rounded-l w-10 h-full flex items-center justify-center bg-slate-100 border text-slate-500 dark:bg-darkmode-700 dark:border-darkmode-800 dark:text-slate-400" style="height: 42px;">
                       <i data-lucide="calendar" class="w-4 h-4"></i>
                    </div>
                      <input type="text" class="datepicker pl-12" data-single-mode="true" style="width: 100%!important;">
                    </div>
                    <div class="col-span-12">
                        <label for="pos-form-2" class="form-label">Description</label>
                        <textarea id="update-profile-form-5" class="form-control" placeholder="Description"></textarea>
                    </div>
                    <div class="col-span-12">
                        <label for="pos-form-3" class="form-label">Upload File</label>
                        <input id="pos-form-3" type="file" class="form-control flex-1" placeholder="Upload File">
                    </div>
                </div>
                <div class="modal-footer text-right">
                    <button type="button" data-tw-dismiss="modal" class="btn btn-outline-secondary w-32 mr-1">Cancel</button>
                    <button type="button" class="btn btn-primary w-32">Submit</button>
                </div>
            </div>
        </div>
    </div>
    <!-- END: New Order Modal -->
    <style>
        .dark-mode-switcher{
            display: none;
        }
        .ref{
            text-align: center!important;
        }
        .mob
        {
            text-align:center!important;
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