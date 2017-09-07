<!DOCTYPE html>
<html lang="en">
<head>
<link rel="stylesheet" type = "text/css" href="{{ url_for('static', filename='stylesheets/main.css') }}">
</head>
<body>
    <div id ="main">
     <h3>Control a LED via Web</h3>
      <div id ="buttons">
       <form action="" method="POST">
         <input type="submit" name="On" value="On" />
         <input type="submit" name="Off" value="Off" />
       </form> 
      </div>
      <div id="LED-image">
       <?php
         $stat = $_POST['name'];
         if($_POST == "On"){          
          echo '<img src = href="{{ url_for(\'static\', filename=\'images/LED-on.jpg\') }}"';
         elseif($_POST == "Off"){
          echo '<img src = href="{{ url_for(\'static\', filename=\'images/LED-off.jpg\') }}"';
         endif
       ?>  
      </div>
    </div>
</body>
</html>

