<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1 shrink-to-fit=no">
    <title>cool tinder thing</title> <!-- TODO: update me -->
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/css/bootstrap.min.css" integrity="sha384-y3tfxAZXuh4HwSYylfB+J125MxIs6mR5FOHamPBG064zB+AFeWH94NdvaCBm8qnd" crossorigin="anonymous">
    <style>
        .thumbnail{
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 4px;
            transition: border .2s ease-in-out; // doesn't work
        }
        .match {
            border: 2px solid;
            border-radius: 4px;
            padding: 4px;
            margin-bottom: 20px;
        }
    </style>
  </head>
  <body>
    <!-- TODO: move navbar to separate file, CSS to separate file -->
    <%include file="pynder_web:/templates/nav.mako" />
        <div class="container">
        ${self.body()}
        </div> <!-- End Container -->
        <!-- jQuery first, then Bootstrap JS. -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/js/bootstrap.min.js" integrity="sha384-vZ2WRJMwsjRMW/8U7i6PWi6AlO1L79snBrmgiDpgIWJ82z8eA5lenwvxbMV1PAh7" crossorigin="anonymous"></script>
  </body>
</html>

