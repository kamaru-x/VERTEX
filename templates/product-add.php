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
        color: #1e40af;">Add Products</h2>
        
        <div class="px-5 sm:px-20 mt-10 pt-10 border-t border-slate-200/60 dark:border-darkmode-400">
            <!-- <div class="font-medium text-base">Add / Manage Products</div> -->
            <div class="grid grid-cols-12 gap-4 gap-y-5 mt-5">
                <div class="intro-y col-span-12 sm:col-span-6">
                        <!-- <div class="mt-3"> -->
                        <label>Select Category</label>
                        <div class="mt-2">
                            <select data-placeholder="Select your favorite actors" class="tom-select w-full">
                                <option>Category 1</option>
                                <option>Category 2</option>
                                <option>Category 3</option>
                                <option>Category 4</option>
                            </select>
                        </div>
                    <!-- </div> -->
                </div>
                <div class="intro-y col-span-12 sm:col-span-6">
                    <label for="input-wizard-2" class="form-label">Enter Product Title</label>
                    <input id="input-wizard-2" type="text" class="form-control" placeholder="Name">
                </div>
                <div class="intro-y col-span-12 sm:col-span-6">
                    <label for="input-wizard-3" class="form-label">Enter Product Price</label>
                    <input id="input-wizard-3" type="text" class="form-control" placeholder="Price">
                </div>
                <div class="intro-y col-span-12 sm:col-span-6">
                    <label for="input-wizard-4" class="form-label">Product Ref.</label>
                    <input id="input-wizard-4" type="text" class="form-control" placeholder="Reference">
                </div>
                
                <div class="intro-y col-span-12 flex items-center justify-center sm:justify-end mt-5">
                    <!-- <button class="btn btn-secondary w-24">Add</button> -->
                    <button class="btn btn-primary w-24 ml-2">Submit</button>
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