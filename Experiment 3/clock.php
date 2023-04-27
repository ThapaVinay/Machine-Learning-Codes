<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="clock.css">
    <title>Clock</title>
    <script>
            setInterval(() => {
                let d = new Date();
                let date = d.toLocaleDateString();
                let time = String(d.getHours()).padStart(2,'0') + ":" + String(d.getMinutes()).padStart(2,'0') + ":" + String(d.getSeconds()).padStart(2,'0') ;
                document.getElementById('span').innerHTML = time + "<br>" + date; 
            }, 1000);
    </script>
</head>
<body>
    <h1> Current time is : </h1>    
    <div id = "div">
        <div id = "span">
            <script>
                let d = new Date();
                let date = d.toLocaleDateString();
                let time = String(d.getHours()).padStart(2,'0') + ":" + String(d.getMinutes()).padStart(2,'0') + ":" + String(d.getSeconds()).padStart(2,'0') ;
                document.getElementById('span').innerHTML = time + "<br>" + date; 
            </script>
        </div>
    </div>
</body>
</html>