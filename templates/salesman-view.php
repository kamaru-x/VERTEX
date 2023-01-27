
<!DOCTYPE html>

<html lang="en" class="light">
    <!-- BEGIN: Head -->
    <head>
        <meta charset="utf-8">
        <link href="dist/images/logo.svg" rel="shortcut icon">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="Midone admin is super flexible, powerful, clean & modern responsive tailwind admin template with unlimited possibilities.">
        <meta name="keywords" content="admin template, Midone Admin Template, dashboard template, flat admin template, responsive admin template, web app">
        <meta name="author" content="LEFT4CODE">
        <title>Dashboard - Midone - Tailwind HTML Admin Template</title>
        <!-- BEGIN: CSS Assets-->
        <link rel="stylesheet" href="dist/css/app.css" />
        <!-- END: CSS Assets-->
    </head>
    <!-- END: Head -->
    <body class="py-5">
        <?php
            include("header.php");
        ?>
        <!-- BEGIN: Content -->
        <div class="content">
            <div class="relative">
                <div class="grid grid-cols-12 gap-6">
                    <div class="col-span-12 xl:col-span-9 2xl:col-span-9 z-10">
                        <div class="mt-6 -mb-6 intro-y">
                            <!-- <div class="alert alert-dismissible show box bg-danger text-white flex items-center mb-6" role="alert">
                                <span>
                                     You have 3 tasks pending!
                                </span>
                                <button type="button" class="btn-close text-white" data-tw-dismiss="alert" aria-label="Close"> <i data-lucide="x" class="w-4 h-4"></i> </button>
                            </div> -->
                            <div class="alert alert-danger show flex items-center mb-2" role="alert"> <i data-lucide="alert-circle" class="w-6 h-6 mr-2"></i> You have 3 tasks pending!<button type="button" class="btn-close text-white" data-tw-dismiss="alert" aria-label="Close"> <i data-lucide="x" class="w-4 h-4"></i> </button></div>
                        </div>
                        <div class="mt-14 mb-3 grid grid-cols-12 sm:gap-10 intro-y" style="background: #fff;">
                            <div class="col-span-12 sm:col-span-6 md:col-span-4 py-6 sm:pl-5 md:pl-0 lg:pl-5 relative text-center sm:text-left">
                                <div class="absolute pt-0.5 2xl:pt-0 mt-5 2xl:mt-6 top-0 right-0 dropdown">
                                    <a class="dropdown-toggle block" href="javascript:;" aria-expanded="false" data-tw-toggle="dropdown"> <i data-lucide="more-vertical" class="w-5 h-5 text-slate-500"></i> </a>
                                    <div class="dropdown-menu w-40">
                                        <ul class="dropdown-content">
                                            <li>
                                                <a href="" class="dropdown-item"> <i data-lucide="file-text" class="w-4 h-4 mr-2"></i> Monthly Report </a>
                                            </li>
                                            <li>
                                                <a href="" class="dropdown-item"> <i data-lucide="file-text" class="w-4 h-4 mr-2"></i> Annual Report </a>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                                <div class="text-sm 2xl:text-base font-medium -mb-1 text-primary"> Hi Ramshad Hassan, <span class="text-slate-600 dark:text-slate-300 font-normal">welcome back!</span> </div>
                                <div class="text-base 2xl:text-lg justify-center sm:justify-start flex items-center text-slate-600 dark:text-slate-300 leading-3 mt-14 2xl:mt-24"> Total Target Assigned <i data-lucide="alert-circle" class="tooltip w-5 h-5 ml-1.5 mt-0.5" title="Total value of your sales: $158.409.416"></i> </div>
                                <div class="2xl:flex mt-5 mb-3">
                                    <div class="flex items-center justify-center sm:justify-start">
                                        <div class="relative text-2xl 2xl:text-3xl font-medium leading-6 pl-3 2xl:pl-4 text-primary"> <span class="absolute text-xl 2xl:text-2xl top-0 left-0 -mt-1 2xl:mt-0 ">$</span> 142,402,210 </div>
                                        <a class="text-slate-500 ml-4 2xl:ml-16" href=""> <i data-lucide="refresh-ccw" class="w-4 h-4"></i> </a>
                                    </div>
                                    <div class="mt-5 2xl:flex 2xl:justify-center 2xl:mt-0 2xl:-ml-20 2xl:w-14 2xl:flex-none 2xl:pl-2.5">
                                        <div class="font-medium inline-flex bg-success text-white rounded-full px-2 py-1 text-xs 2xl:text-sm 2xl:p-0 2xl:text-success 2xl:bg-transparent 2xl:flex items-center tooltip cursor-pointer 2xl:justify-center" title="49% Higher than last month"> 49% <i data-lucide="chevron-up" class="w-4 h-4 ml-0.5"></i> </div>
                                    </div>
                                </div>
                                
                                <div class="2xl:text-base text-slate-600 dark:text-slate-300 mt-6 -mb-1 "> Target Achieved <a href="" class="underline decoration-dotted underline-offset-4 text-success dark:text-slate-400">$12,921,050</a> </div>
                                <div class="2xl:text-base text-slate-600 dark:text-slate-300 mt-6 -mb-1">  Target Failed <a href="" class="underline decoration-dotted underline-offset-4 text-danger dark:text-slate-400">$2,921,050</a> </div>
                                
                            </div>

                             <div class="row-start-2 md:row-start-auto col-span-12 md:col-span-6 py-6 border-black border-opacity-10 border-t md:border-t-0 md:border-l md:border-r border-dashed px-10 sm:px-28 md:px-5 -mx-5">
                                <div class="flex flex-wrap items-center">
                                    <div class="flex items-center w-full sm:w-auto justify-center sm:justify-start mr-auto mb-5 2xl:mb-0">
                                        
                                        <!-- <div class="ml-3.5">
                                            <div class="relative text-xl 2xl:text-2xl font-medium leading-6 2xl:leading-5 pl-3.5 2xl:pl-4"> <span class="absolute text-base 2xl:text-xl top-0 left-0 2xl:-mt-1.5">$</span> 47,578.77 </div>
                                            <div class="text-slate-500 mt-2">Yearly budget</div>
                                        </div> -->
                                    </div>
                                    
                                </div>
                               <!--  <div class="mt-10 text-slate-600 dark:text-slate-300">You have spent about 35% of your annual budget.</div> -->
                                <div class="mt-6">
                                    <div class="h-[290px]">
                                       <canvas id="report-line-chart" class="mt-6 -mb-6"></canvas>
                                    </div>
                                </div>
                            </div> 

                           
                        </div>
                    </div>
                   
                </div>
                <div class="report-box-4 w-full h-full grid grid-cols-12 gap-6 xl:absolute -mt-8 xl:mt-0 pb-6 xl:pb-0 top-0 right-0 z-30 xl:z-auto">
                    <div class="col-span-12 xl:col-span-3 xl:col-start-10 xl:pb-16 z-30">
                        <div class="h-full flex flex-col">
                            
                            <div class="report-box-4__content xl:min-h-0 intro-x">
                                <div class="max-h-full xl:overflow-y-auto box mt-5">
                                    <div class="xl:sticky top-0 px-5 pt-5 pb-6">
                                        <div class="flex items-center">
                                            <div class="text-lg font-medium truncate mr-5">Taskbar</div>
                                            <a href="" class="ml-auto flex items-center text-primary"> <i data-lucide="refresh-ccw" class="w-4 h-4 mr-3"></i> Refresh </a>
                                        </div>
                                        
                                    </div>
                                    <div class="tab-content px-5 pb-5">
                                        <div class="tab-pane active grid grid-cols-12 gap-y-6" id="weekly-report" role="tabpanel" aria-labelledby="weekly-report-tab">
                                            <div class="col-span-12 sm:col-span-6 md:col-span-4 xl:col-span-12">
                                                <div class="text-slate-500 task-head">TASK 1</div>
                                                <div class="mt-1.5 flex items-center">
                                                  <i data-lucide="alert-triangle" class="w-4 h-4 mr-1 text-danger"></i>
                                                    <!-- <div class="text-lg">Task Description here</div> -->
                                                    <div class="text-danger flex text-xs font-medium tooltip cursor-pointer ml-2" title="Urgent Task"> Due within 3 days</div>
                                                </div>
                                            </div>
                                            <div class="col-span-12 sm:col-span-6 md:col-span-4 xl:col-span-12">
                                                <div class="text-slate-500 task-head">TASK 2</div>
                                                <div class="mt-1.5 flex items-center">
                                                  <i data-lucide="alert-triangle" class="w-4 h-4 mr-1 text-danger"></i>
                                                    <!-- <div class="text-lg">Task Description here</div> -->
                                                    <div class="text-danger flex text-xs font-medium tooltip cursor-pointer ml-2" title="Urgent Task"> Due within 5 days </div>
                                                </div>
                                            </div>
                                           <div class="col-span-12 sm:col-span-6 md:col-span-4 xl:col-span-12">
                                                <div class="text-slate-500 task-head">TASK 3</div>
                                                <div class="mt-1.5 flex items-center">
                                                  <i data-lucide="alert-triangle" class="w-4 h-4 mr-1 text-danger"></i>
                                                    <!-- <div class="text-lg">Task Description here</div> -->
                                                    <div class="text-danger flex text-xs font-medium tooltip cursor-pointer ml-2" title="Urgent Task"> Due Within 3 days</div>
                                                </div>
                                            </div>
                                            
                                            
                                            <div class="col-span-12 sm:col-span-6 md:col-span-4 xl:col-span-12">
                                                <div class="text-slate-500 task-head">TASK 4</div>
                                                <div class="mt-1.5 flex items-center">
                                                  <i data-lucide="alert-triangle" class="w-4 h-4 mr-1 text-danger"></i>
                                                    <!-- <div class="text-lg">Task Description here</div> -->
                                                    <div class="text-danger flex text-xs font-medium tooltip cursor-pointer ml-2" title="Urgent Task"> Due within 3 days</div>
                                                </div>
                                            </div>
                                            <button class="btn btn-outline-secondary col-span-12 border-slate-300 dark:border-darkmode-300 border-dashed relative justify-start mb-2"><a href="task-pending.php">
                                                <span class="truncate mr-5">View All Tasks</span> 
                                                <span class="w-8 h-8 absolute flex justify-center items-center right-0 top-0 bottom-0 my-auto ml-auto mr-0.5"> <i data-lucide="arrow-right" class="w-4 h-4"></i> </span></a>
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <style>
                .task-head{
                    font-weight: 600;
                    color: #1f41af;
                }
            </style>
            <!-- <div class="report-box-3 report-box-3--content grid grid-cols-12 gap-6 xl:-mt-5 2xl:-mt-8 -mb-10 z-40 2xl:z-10">
                <div class="col-span-12 2xl:col-span-9">
                    <div class="grid grid-cols-12 gap-6"> -->
                        <!-- BEGIN: Wizard Layout -->
    <div class="intro-y box py-10 sm:py-20 mt-5">
        
        <br><br><hr>
        <!-- <h2 class="intro-y text-lg font-medium mt-10" style="text-align: center;font-size: 35px;color:#1e40af;padding-bottom: 30px;border-bottom: solid 1px #bcbcbc21;">Proposal</h2>
 -->
                        <div class="container" style="padding: 40px;">
<ul class="nav nav-link-tabs" role="tablist">
    <li id="example-5-tab" class="nav-item flex-1" role="presentation">
        <button class="nav-link w-full py-2 active" data-tw-toggle="pill" data-tw-target="#example-tab-5" type="button" role="tab" aria-controls="example-tab-5" aria-selected="true">
            Lead
        </button>
    </li>
    <li id="example-6-tab" class="nav-item flex-1" role="presentation">
        <button class="nav-link w-full py-2" data-tw-toggle="pill" data-tw-target="#example-tab-6" type="button" role="tab" aria-controls="example-tab-6" aria-selected="false">
            Opportunity
        </button>
    </li>
    <li id="example-7-tab" class="nav-item flex-1" role="presentation">
        <button class="nav-link w-full py-2" data-tw-toggle="pill" data-tw-target="#example-tab-7" type="button" role="tab" aria-controls="example-tab-5" aria-selected="true">
            Clients
        </button>
    </li>
    <li id="example-8-tab" class="nav-item flex-1" role="presentation">
        <button class="nav-link w-full py-2" data-tw-toggle="pill" data-tw-target="#example-tab-8" type="button" role="tab" aria-controls="example-tab-5" aria-selected="true">
            Projects
        </button>
    </li>
    
    <!-- <li id="example-10-tab" class="nav-item flex-1" role="presentation">
        <button class="nav-link w-full py-2" data-tw-toggle="pill" data-tw-target="#example-tab-10" type="button" role="tab" aria-controls="example-tab-5" aria-selected="true">
          Opportunity Info
        </button>
    </li> -->
    
</ul>
<div class="tab-content mt-5">
    <div id="example-tab-5" class="tab-pane leading-relaxed active" role="tabpanel" aria-labelledby="example-5-tab">
        
       
    <h2 class="intro-y text-lg font-medium mt-10" style="text-align: center;font-size: 35px;color:#1e40af;padding-top: 30px;padding-bottom: 30px;border-bottom: solid 1px #bcbcbc;">List Of Leads</h2>
         <!--   <div class="intro-y box py-10 sm:py-20 mt-5">
        <h2 style=" font-size: 30px; font-weight: 500; text-align: center;
        color: #1e40af;">Add Category</h2>
    </div> -->
    <div class="grid grid-cols-12 gap-6 mt-5">
        <div class="intro-y col-span-12 flex flex-wrap xl:flex-nowrap items-center mt-2">
            
            <div class="hidden xl:block mx-auto text-slate-500"></div>
            <div class="w-full xl:w-auto flex items-center mt-3 xl:mt-0">
                <button class="btn btn-primary shadow-md mr-2">
                    <i data-lucide="file-text" class="w-4 h-4 mr-2"></i> Export to Excel
                </button>
             
            </div>
        </div>
         <!-- BEGIN: Data List -->
        <div class="intro-y col-span-12 overflow-auto 2xl:overflow-visible">
            <table class="table table-report -mt-2">
                <thead>
                    <tr>
                        <!-- <th class="whitespace-nowrap">
                            <input class="form-check-input" type="checkbox">
                        </th> -->
                        <th class="whitespace-nowrap">SL. NO.</th>
                        <th class="whitespace-nowrap">COMPANY NAME</th>
                        <th class="whitespace-nowrap">PRIMARY CONTACT</th>
                        <th class="whitespace-nowrap">SALESMAN</th>
                        <th class="text-center whitespace-nowrap">TOTAL MEETINGS</th>
                        <th class="text-center whitespace-nowrap">SUMMARY</th>
                        
                    </tr>
                </thead>
                <tbody>
                        <tr class="intro-x">
                            
                            <td class="w-20">
                                <a href="" class=" whitespace-nowrap">1</a>
                            </td>
                            <td class="w-60">
                                <a href="leads-view.php" class="font-medium whitespace-nowrap text-primary">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                
                            </td>
                            <td class="w-60">
                                <div class="font-medium whitespace-nowrap">Vijesh Chandran</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">5534 6688</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">vijesh@abcdintl.com</div>
                            </td>
                            <td class="w-60">
                                <a href="salesman-list.php" class="font-medium whitespace-nowrap">Ramshad Hassan</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">5500 3488</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">ramshad@vertex.com.qa</div>
                            </td>
                            <td class="text-center">
                                <div class="flex items-center justify-center whitespace-nowrap"><span>Done: 3</span></div> 
                                <div class="flex items-center justify-center whitespace-nowrap"><span class="text-success">Upcoming: 2</span></div>
                            </td>
                            <td class="text-center">
                                <div class="flex items-center justify-center whitespace-nowrap"><span>Lead Created on: 24 Dec 2022</span></div>
                                <div class="flex items-center justify-center whitespace-nowrap"><span class="text-primary">Expected Value: 350,000.00</span></div>
                                <div class="flex items-center justify-center whitespace-nowrap"><span class="text-danger">Expected Closing: 23 Jan 2023</span></div>
                            </td>
                            
                            
                        </tr>


                        <tr class="intro-x">
                            
                            <td class="w-20">
                                <a href="" class=" whitespace-nowrap">2</a>
                            </td>
                            <td class="w-60">
                                <a href="leads-view.php" class="font-medium whitespace-nowrap text-primary">XYZ International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                               
                            </td>
                            <td class="w-60">
                                 <div class="font-medium whitespace-nowrap">Vijesh Chandran</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">5534 6688</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">vijesh@abcdintl.com</div>
                            </td>
                            <td class="w-60">
                                <a href="salesman-list.php" class="font-medium whitespace-nowrap">Ramshad Hassan</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">5500 3488</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">ramshad@vertex.com.qa</div>
                            </td>
                            <td class="text-center">
                                <div class="flex items-center justify-center whitespace-nowrap"><span>Done: 3</span></div> 
                                <div class="flex items-center justify-center whitespace-nowrap"><span class="text-success">Upcoming: 2</span></div>
                            </td>
                            <td class="text-center">
                                <div class="flex items-center justify-center whitespace-nowrap"><span>Lead Created on: 24 Dec 2022</span></div>
                                <div class="flex items-center justify-center whitespace-nowrap"><span class="text-primary">Expected Value: 350,000.00</span></div>
                                <div class="flex items-center justify-center whitespace-nowrap"><span class="text-danger">Expected Closing: 23 Jan 2023</span></div>
                            </td>
                            
                            
                        </tr>


                        <tr class="intro-x">
                            
                            <td class="w-20">
                                <a href="" class=" whitespace-nowrap">3</a>
                            </td>
                            <td class="w-60">
                                <a href="leads-view.php" class="font-medium whitespace-nowrap text-primary">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                
                            </td>
                            <td class="w-60">
                                 <div class="font-medium whitespace-nowrap">Vijesh Chandran</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">5534 6688</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">vijesh@abcdintl.com</div>
                            </td>
                            <td class="w-60">
                                <a href="salesman-list.php" class="font-medium whitespace-nowrap">Ramshad Hassan</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">5500 3488</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">ramshad@vertex.com.qa</div>
                            </td>
                            <td class="text-center">
                                <div class="flex items-center justify-center whitespace-nowrap"><span>Done: 3</span></div> 
                                <div class="flex items-center justify-center whitespace-nowrap"><span class="text-success">Upcoming: 2</span></div>
                            </td>
                            <td class="text-center">
                                <div class="flex items-center justify-center whitespace-nowrap"><span>Lead Created on: 24 Dec 2022</span></div>
                                <div class="flex items-center justify-center whitespace-nowrap"><span class="text-primary">Expected Value: 350,000.00</span></div>
                                <div class="flex items-center justify-center whitespace-nowrap"><span class="text-danger">Expected Closing: 23 Jan 2023</span></div>
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
    <!--  -->
    <div id="example-tab-6" class="tab-pane leading-relaxed" role="tabpanel" aria-labelledby="example-6-tab">

        
                     <h2 class="intro-y text-lg font-medium mt-10" style="text-align: center;font-size: 35px;color:#1e40af;padding-top: 30px;padding-bottom: 30px;border-bottom: solid 1px #bcbcbc;">Opportunities</h2>
                     <div class="grid grid-cols-12 gap-6 mt-5">
        <div class="intro-y col-span-12 flex flex-wrap xl:flex-nowrap items-center mt-2">
            
            <div class="hidden xl:block mx-auto text-slate-500"></div>
            <div class="w-full xl:w-auto flex items-center mt-3 xl:mt-0">
                <button class="btn btn-primary shadow-md mr-2">
                    <i data-lucide="file-text" class="w-4 h-4 mr-2"></i> Export to Excel
                </button>
              
            </div>
        </div>
        <!-- BEGIN: Data List -->
        <div class="intro-y col-span-12 overflow-auto 2xl:overflow-visible">
            <table class="table table-report -mt-2">
                <thead>
                    <tr>
                        <!-- <th class="whitespace-nowrap">
                            <input class="form-check-input" type="checkbox">
                        </th> -->
                        <th class="whitespace-nowrap">COMPANY NAME</th>
                        <th class="whitespace-nowrap">REFERENCE (LEAD REFERENCE)</th>
                        <th class="text-center whitespace-nowrap">DATE OF OPPORTUNITY CONVERSION</th>
                        
                        <th class="whitespace-nowrap">
                            <div class="pr-16">SALESMAN</div>
                        </th>
                        
                    </tr>
                </thead>
                <tbody>
                       

                      


                        <tr class="intro-x">
                           
                             <td class="w-60">
                                <a href="opportunity-view.php" class="font-medium whitespace-nowrap text-primary">XYZ International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                
                            </td>
                            <td class="w-60 text-center">
                                  <a href="" class="font-medium whitespace-nowrap ">REF:12345</a>
                                
                            </td>
                            </td>
                            <td class="text-center">
                                <div class="flex items-center justify-center whitespace-nowrap text-success">
                                     2/10/2023
                                </div>
                            </td>
                            
                            <td class="w-60">
                                <a href="salesman-view.php" class="font-medium whitespace-nowrap text-primary text-primary">Ramshad Hassan</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">5534 6688</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">ramshad@vertex.com.qa</div>
                            </td>
                            
                            
                        </tr>

                        <tr class="intro-x">
                            
                            <td class="w-60">
                                <a href="opportunity-view.php" class="font-medium whitespace-nowrap text-primary">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                </div>
                            </td>
                            <td class="w-60 text-center">
                                 <a href="" class="font-medium whitespace-nowrap">REF:12345</a>
                                 
                            </td>
                            </td>
                            <td class="text-center">
                                <div class="flex items-center justify-center whitespace-nowrap text-success">
                                     2/10/2023
                                </div>
                            </td>
                          
                            <td class="w-60">
                                <a href="salesman-view.php" class="font-medium whitespace-nowrap text-primary">Ramshad Hassan</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">5534 6688</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">ramshad@vertex.com.qa</div>
                            </td>
                            
                              
                        </tr>

                        <tr class="intro-x">
                            <!-- <td class="w-10">
                                <input class="form-check-input" type="checkbox">
                            </td> -->
                            <td class="w-60">
                                <a href="opportunity-view.php" class="font-medium whitespace-nowrap text-primary">XYZ International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                
                            </td>
                            <td class="w-60 text-center">
                                 <a href="" class="font-medium whitespace-nowrap">REF:12345</a>
                                
                            </td>
                            </td>
                            <td class="text-center">
                                <div class="flex items-center justify-center whitespace-nowrap text-success">
                                     2/10/2023
                                </div>
                            </td>
                            
                            <td class="w-60">
                                <a href="salesman-view.php" class="font-medium whitespace-nowrap text-primary">Ramshad Hassan</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">5534 6688</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">ramshad@vertex.com.qa</div>
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

    <!-- Timeline -->

    <div id="example-tab-7" class="tab-pane leading-relaxed" role="tabpanel" aria-labelledby="example-7-tab">

        <div class="post__content tab-content">
                       <h2 class="intro-y text-lg font-medium mt-10" style="text-align: center;font-size: 35px;color:#1e40af;padding-top: 30px;padding-bottom: 30px;border-bottom: solid 1px #bcbcbc;">Clients</h2>
    <div class="grid grid-cols-12 gap-6 mt-5">
        <div class="intro-y col-span-12 flex flex-wrap xl:flex-nowrap items-center mt-2">
           
            <!-- <div class="hidden xl:block mx-auto text-slate-500" style="text-align: center;">Showing 1 to 10 of 150 entries</div> -->
            <div class="w-full xl:w-auto flex items-center mt-3 xl:mt-0">
                
            </div>
        </div>
        <!-- BEGIN: Data List -->
        <div class="intro-y col-span-12 overflow-auto 2xl:overflow-visible">
            <table class="table table-report -mt-2">
                <thead>
                    <tr>
                        <!-- <th class="whitespace-nowrap">
                            <input class="form-check-input" type="checkbox">
                        </th> -->
                        
                       
                        <th class="whitespace-nowrap">COMPANY NAME</th>
                         <th class="whitespace-nowrap">REFERENCE </th>
                        
                        <th class="text-center whitespace-nowrap" style="text-align: center;">PROPOSAL DATE</th>
                        <th class="whitespace-nowrap">
                            <div class="pr-16">SALESMAN</div>
                        </th>
                        <th class="whitespace-nowrap" style="text-align: center;">STATUS </th>
                        
                    </tr>
                </thead>
                <tbody>
                            <tr class="intro-x">
                            <!-- <td class="w-10">
                                <input class="form-check-input" type="checkbox">
                            </td> -->
                            <td class="w-72 text-primary">
                                <a href="clients-view.php" class="font-medium whitespace-nowrap">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                               
                            </td>
                            <td class="w-40">
                                <a href="" class="font-medium whitespace-nowrap">REF:12345</a>
                                 
                            </td>
                            
                            <td class="w-60 text-right">
                                <div class="pr-16">23/3/2023</div>
                            </td>
                            <td class="w-60">
                                <a href="" class="font-medium whitespace-nowrap text-primary">Ramshad Hassan</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">5500 3488</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">ramshad@vertex.com.qa</div>
                            </td>
                            <td class="text-center">
                                <div class="flex items-center justify-center whitespace-nowrap text-success">
                                     Confirmed
                                </div>
                            </td>
                            
                            
                        </tr>

                         <tr class="intro-x">
                            
                            <td class="w-72 text-primary">
                                <a href="clients-view.php" class="font-medium whitespace-nowrap">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                
                            </td>
                            <td class="w-40">
                                 <a href="" class="font-medium whitespace-nowrap">REF:12345</a>
                            </td>
                            
                             <td class="w-60 text-right">
                                <div class="pr-16">23/3/2023</div>
                            </td>
                            <td class="w-60">
                                <a href="" class="font-medium whitespace-nowrap text-primary">Ramshad Hassan</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">5500 3488</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">ramshad@vertex.com.qa</div>
                            </td>
                             <td class="text-center">
                                <div class="flex items-center justify-center whitespace-nowrap text-success">
                                     Confirmed
                                </div>
                            </td>
                           
                            
                        </tr>
                                            <tr class="intro-x">
                            <!-- <td class="w-10">
                                <input class="form-check-input" type="checkbox">
                            </td> -->
                            <td class="w-72 text-primary">
                                <a href="clients-view.php" class="font-medium whitespace-nowrap">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                               
                            </td>
                            <td class="w-40">
                                 <a href="" class="font-medium whitespace-nowrap">REF:12345</a>
                            </td>
                            
                            <td class="w-60 text-right">
                                <div class="pr-16">23/3/2023</div>
                            </td>
                            <td class="w-60">
                                <a href="" class="font-medium whitespace-nowrap text-primary">Ramshad Hassan</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">5500 3488</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">ramshad@vertex.com.qa</div>
                            </td>
                             <td class="text-center">
                                <div class="flex items-center justify-center whitespace-nowrap text-success">
                                     Confirmed
                                </div>
                            </td>
                            
                           
                        </tr>
                        <tr class="intro-x">
                           
                            <td class="w-72 text-primary">
                                <a href="clients-view.php" class="font-medium whitespace-nowrap">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                
                            </td>
                            <td class="w-40">
                                 <a href="" class="font-medium whitespace-nowrap">REF:12345</a>
                            </td>
                            
                            <td class="w-60 text-right">
                                <div class="pr-16">23/3/2023</div>
                            </td>
                           <td class="w-60">
                                <a href="" class="font-medium whitespace-nowrap text-primary">Ramshad Hassan</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">5500 3488</div>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">ramshad@vertex.com.qa</div>
                            </td>
                             <td class="text-center ">
                                <div class="flex items-center justify-center whitespace-nowrap text-danger">
                                     Rejected
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
    </div>

    <!-- Status -->
    <div id="example-tab-8" class="tab-pane leading-relaxed" role="tabpanel" aria-labelledby="example-8-tab">

        <div class="post__content tab-content">
                      <h2 class="intro-y text-lg font-medium mt-10" style="text-align: center;font-size: 35px;color:#1e40af;padding-top: 30px;padding-bottom: 30px;border-bottom: solid 1px #bcbcbc;">Projects</h2>
    <div class="grid grid-cols-12 gap-6 mt-5">
        <div class="intro-y col-span-12 flex flex-wrap xl:flex-nowrap items-center mt-2">
           
            <div class="hidden xl:block mx-auto text-slate-500" style="text-align: center;">Showing 1 to 10 of 150 entries</div>
            <div class="w-full xl:w-auto flex items-center mt-3 xl:mt-0">
                
            </div>
        </div>
        <!-- BEGIN: Data List -->
        <div class="intro-y col-span-12 overflow-auto 2xl:overflow-visible">
            <table class="table table-report -mt-2">
                <thead>
                    <tr>
                        <!-- <th class="whitespace-nowrap">
                            <input class="form-check-input" type="checkbox">
                        </th> -->
                        
                       
                        <th class="whitespace-nowrap">COMPANY NAME</th>
                         <th class="whitespace-nowrap">REFERENCE </th>
                        <!-- <th class="text-center whitespace-nowrap" style="text-align: left;">Proposal Date</th> -->
                        <th class="whitespace-nowrap">
                            <div class="pr-16">SALESMAN </div>
                        </th>
                        <th class="whitespace-nowrap">
                            <div class="pr-16">PROPOSAL COMPLETED DATE</div>
                        </th>
                       
                    </tr>
                </thead>
                <tbody>
                            <tr class="intro-x">
                            <!-- <td class="w-10">
                                <input class="form-check-input" type="checkbox">
                            </td> -->
                            <td class="w-72 text-primary">
                                <a href="project-view.php" class="font-medium whitespace-nowrap">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                
                            </td>
                            <td class="w-40">
                                <a href="" class="font-medium whitespace-nowrap">REF:15678</a>
                            </td>
                                 
                           
                            
                            <td class="w-64">
                             <a href="salesman-view.php" class="font-medium whitespace-nowrap text-primary">Ramshad Hassan</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4466 7877 / ramshad@vertex.com.qa</div>
                            </td>

                             <td class="w-40" style="text-align:center;">
                                <div  class="font-medium whitespace-nowrap text-success">12/3/2023</div>
                            </td>
                            
                             
                        </tr>

                         <tr class="intro-x">
                            
                            <td class="w-72 text-primary">
                                <a href="project-view.php" class="font-medium whitespace-nowrap">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                
                            </td>
                            <td class="w-40">
                                <a href="" class="font-medium whitespace-nowrap">REF:15678</a>
                            </td>
                            
                            
                            <td class="w-64">
                             <a href="salesman-view.php" class="font-medium whitespace-nowrap text-primary">Ramshad Hassan</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4466 7877 / ramshad@vertex.com.qa</div>
                            </td>
                           
                           <td class="w-40" style="text-align:center;">
                                <a href="" class="font-medium whitespace-nowrap text-success">12/3/2023</a>
                            </td>

                            
                        </tr>

                         <tr class="intro-x">
                            <!-- <td class="w-10">
                                <input class="form-check-input" type="checkbox">
                            </td> -->
                           <td class="w-72 text-primary">
                                <a href="project-view.php" class="font-medium whitespace-nowrap">ABCD International</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4433 6688 / info@abcdintl.com</div>
                                
                            </td>
                            <td class="w-40">
                                <a href="" class="font-medium whitespace-nowrap">REF:15678</a>
                            </td>
                           
                            
                            <td class="w-64">
                             <a href="salesman-view.php" class="font-medium whitespace-nowrap text-primary">Ramshad Hassan</a>
                                <div class="text-slate-500 text-xs whitespace-nowrap mt-0.5">4466 7877 / ramshad@vertex.com.qa</div>
                            </td>

                            <td class="w-40" style="text-align:center;">
                                 <div  class="font-medium whitespace-nowrap text-success">12/3/2023</div>
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
</div>

    


<!-- previous meeting -->

<h2 style=" font-size: 30px; font-weight: 500; text-align: center;
        color: #1e40af; padding-top: 100px; padding-bottom:10px;">Previous Meeting</h2>
         <div  style="float:right; margin-right:20px;"><a href="#" data-tw-toggle="modal" data-tw-target="#new-order-modal1"><button class="btn btn-primary shadow-md mr-2">Add Schedule</button></a></div><br><br><br>
                                    
                                        <div class="overflow-x-auto">
                                            <table class="table">
                                                <thead class="table-dark">
                                                    <tr>
                                                        <th class="whitespace-nowrap">Date</th>
                                                        <th class="whitespace-nowrap">Company Name</th>
                                                        <th class="whitespace-nowrap">Salesman</th>
                                                        <th class="whitespace-nowrap">Mode Of Meeting</th>
                                                        <th class="whitespace-nowrap">Time </th>
                                                        <th>Updates</th>
                                                        <th class="whitespace-nowrap">Remark</th>
                                                       
                                                         <th>Action</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <td>1/12/2023</td>
                                                         <td class="text-primary">ABC International<br>4433 6688 / info@abcdintl.com</td>
                                                        <td>Ramshad Hassan<br>
                                                         ID#12345</td>
                                                        <td>Online</td>
                                                        <td class="text-primary">10:00 AM - 12:00 PM</td>
                                                         <td class="text-primary">
                                                        <a href="#" data-tw-toggle="modal" data-tw-target="#new-order-modal2 ">Add Update</a>  
                                                     </td>
                                                        
                                                        <td>Status updated</td>
                                                       <td> <a class="flex items-center text-primary whitespace-nowrap mr-5" href="meeting-previous-details.php" title="view">
                                                    <i data-lucide="eye" class="w-4 h-4 mr-1"></i> 
                                                    </a></td>
                                                    </tr>
                                                     <tr>
                                                        <td>1/12/2023</td>
                                                         <td class="text-primary">ABC International<br>4433 6688 / info@abcdintl.com</td>
                                                        <td>Ramshad Hassan<br>
                                                         ID#12345</td>
                                                        <td>Online</td>
                                                        <td class="text-primary">10:00 AM - 12:00 PM</td>
                                                         <td class="text-primary">
                                                        <a href="#" data-tw-toggle="modal" data-tw-target="#new-order-modal2 ">Add Update</a>  
                                                     </td>
                                                        
                                                        <td>Status updated</td>
                                                       <td> <a class="flex items-center text-primary whitespace-nowrap mr-5" href="meeting-previous-details.php" title="view">
                                                    <i data-lucide="eye" class="w-4 h-4 mr-1"></i> 
                                                    </a></td>
                                                    </tr>
                                                     <tr>
                                                        <td>1/12/2023</td>
                                                         <td class="text-primary">ABC International<br>4433 6688 / info@abcdintl.com</td>
                                                        <td>Ramshad Hassan<br>
                                                         ID#12345</td>
                                                        <td>Online</td>
                                                        <td class="text-primary">10:00 AM - 12:00 PM</td>
                                                         <td class="text-primary">
                                                        <a href="#" data-tw-toggle="modal" data-tw-target="#new-order-modal2 ">Add Update</a>  
                                                     </td>
                                                        
                                                        <td>Status updated</td>
                                                       <td> <a class="flex items-center text-primary whitespace-nowrap mr-5" href="meeting-previous-details.php" title="view">
                                                    <i data-lucide="eye" class="w-4 h-4 mr-1"></i> 
                                                    </a></td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    


<!-- /previous meeting -->
<!-- upcoming meeting -->
 
<h2 style=" font-size: 30px; font-weight: 500; text-align: center;
        color: #1e40af; padding-top: 100px; padding-bottom:60px;">Upcoming Meeting</h2>

       
                                <div>
                                    
                                        <div class="overflow-x-auto">
                                            <table class="table">
                                                <thead class="table-dark">
                                                    <tr>
                                                        <th class="whitespace-nowrap">Date</th>
                                                        <th class="whitespace-nowrap">Company Name</th>
                                                        <th class="whitespace-nowrap">Salesman Name</th>
                                                        <th class="whitespace-nowrap">Mode Of Meeting</th>
                                                        <th class="whitespace-nowrap">Time </th>
                                                        
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <td>1/12/2023</td>
                                                         <td class="text-primary">ABC International<br>4433 6688 / info@abcdintl.com</td>
                                                        <td>Ramshad Hassan<br>
                                                         ID#12345</td>
                                                        <td>Direct</td>
                                                        <td class="text-primary">10:00 AM - 12:00 PM</td>
                                                       
                                                    </tr>
                                                    <tr>
                                                        <td>1/12/2023</td>
                                                         <td class="text-primary">ABC International<br>4433 6688 / info@abcdintl.com</td>
                                                        <td>Ramshad Hassan<br>
                                                         ID#12345</td>
                                                        <td>Online</td>
                                                        <td class="text-primary">10:00 AM - 12:00 PM</td>
                                                       
                                                    </tr>
                                                    <tr>
                                                        <td>1/12/2023</td>
                                                         <td class="text-primary">ABC International<br>4433 6688 / info@abcdintl.com</td>
                                                        <td>Ramshad Hassan<br>
                                                         ID#12345</td>
                                                        <td>Telephone</td>
                                                        <td class="text-primary">10:00 AM - 12:00 PM</td>
                                                       
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    

</div>
</div>  
</div> 



    <!-- END: Wizard Layout -->
    </div>
                            <!-- END: Transactions -->
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- END: Content -->
         <!-- BEGIN: New Order Modal -->
    <div id="new-order-modal1" class="modal" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h2 class="font-medium text-base mr-auto">Add Schedule</h2>
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
                    <label>Mode Of Meeting</label>
                        <div class="mt-2">
                            <select data-placeholder="Select Mode Of Meeting" class="tom-select w-full">
                                            <option>Online</option>
                                            <option>Direct</option>
                                            <option>Telephone</option>
                            </select>
                        </div>
                    </div>
                    <div class="col-span-12">
                        <label for="pos-form-2" class="form-label">Time(From)</label>
                        <input id="pos-form-2" type="text" class="form-control flex-1" placeholder="Time(From)">
                    </div>

                    <div class="col-span-12">
                        <label for="pos-form-2" class="form-label">Time(To)</label>
                        <input id="pos-form-2" type="text" class="form-control flex-1" placeholder="Time(To)">
                    </div>
                    
                     <div class="col-span-12">
                        <label for="pos-form-2" class="form-label">Description</label>
                       <textarea id="update-profile-form-5" class="form-control" placeholder="Description"></textarea>
                    </div>
                </div>
                <div class="modal-footer text-right">
                    <button type="button" data-tw-dismiss="modal" class="btn btn-outline-secondary w-32 mr-1">Cancel</button>
                    <button type="button" class="btn btn-primary w-32">Add Schedule</button>
                </div>
            </div>
        </div>
    </div>
    <!-- END: New Order Modal -->
        <!-- BEGIN: Dark Mode Switcher-->
        <div data-url="top-menu-dark-dashboard-overview-3.html" class="dark-mode-switcher cursor-pointer shadow-md fixed bottom-0 right-0 box border rounded-full w-40 h-12 flex items-center justify-center z-50 mb-10 mr-10">
            <div class="mr-4 text-slate-600 dark:text-slate-200">Dark Mode</div>
            <div class="dark-mode-switcher__toggle border"></div>
        </div>
        <!-- END: Dark Mode Switcher-->
        <style>
        .dark-mode-switcher{
            display: none;
        }
        
        </style>
        
        <!-- BEGIN: JS Assets-->
        <script src="https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/markerclusterer.js"></script>
        <script src="https://maps.googleapis.com/maps/api/js?key=["your-google-map-api"]&libraries=places"></script>
        <script src="dist/js/app.js"></script>
        <!-- END: JS Assets-->
    </body>
</html>