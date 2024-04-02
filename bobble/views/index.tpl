% rebase('layout.tpl', title='Home Page', year=year)

<div class="jumbotron">
    <h1>Bottle</h1>
    <p class="lead">Bottle is a free web framework for building great Web sites and Web applications using HTML, CSS and JavaScript.</p>
    <p><a href="http://bottlepy.org/docs/dev/index.html" class="btn btn-primary btn-large">Learn more &raquo;</a></p>
</div>

<div class="row">
    <div class="col-md-4">
        <h2>Getting started</h2>
        <p>
            Bottle gives you a powerful, patterns-based way to build dynamic websites that
            enables a clean separation of concerns and gives you full control over markup
            for enjoyable, agile development.
        </p>
        <p><a class="btn btn-default" href="http://bottlepy.org/docs/dev/index.html">Learn more &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Get more libraries</h2>
        <p>The Python Package Index is a repository of software for the Python programming language.</p>
        <p><a class="btn btn-default" href="https://pypi.python.org/pypi">Learn more &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Microsoft Azure</h2>
        <p>You can easily publish to Microsoft Azure using Visual Studio. Find out how you can host your application using a free trial today.</p>
        <p><a class="btn btn-default" href="http://azure.microsoft.com">Learn more &raquo;</a></p>
    </div>
</div>

<h3> Ask a Question </h3>
        <form id="myForm" action="/home" method="post">
            <div id="errorMessages"></div>
            <p><textarea style="resize: none" rows="2" cols="50" name="QUEST" placeholder="Your question"></textarea></p> 
            <p><input type="text" size="50" name="NAME" placeholder="Your name"></p>
            <p><input type="text" size="50" name="ADRESS" placeholder="Your email"></p>
            <p><input type="date" name="DATE" placeholder="Date"></p>
            <p><input type="submit" value="Send" class="btn btn-default"></p>
        </form>
        <div id="errorMessages"></div>

        <script>
        document.getElementById('myForm').addEventListener('submit', function(event) {
            var errorMessages = document.getElementById('errorMessages');
            errorMessages.innerHTML = '';

            var QUEST = document.getElementsByName('QUEST')[0].value;
            var NAME = document.getElementsByName('NAME')[0].value;
            var ADRESS = document.getElementsByName('ADRESS')[0].value;
            var DATE = document.getElementsByName('DATE')[0].value;

            if (!QUEST || !NAME || !ADRESS || !DATE) {
                errorMessages.innerHTML = '<p style="color: red; font-weight: bold;">All fields are required.</p>';
                event.preventDefault();
            } else {
                var emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
                if (!emailPattern.test(ADRESS)) {
                    errorMessages.innerHTML = '<p style="color: red; font-weight: bold;">Please enter a valid email address.</p>';
                    event.preventDefault();
                } else {
                    var currentDate = new Date().toISOString().split('T')[0];
                    if (DATE > currentDate) {
                        errorMessages.innerHTML = '<p style="color: red; font-weight: bold;">Date cannot be in the future.</p>';
                        event.preventDefault();
                    } else {
                        var year = new Date(DATE).getFullYear();
                        if (year < 2000) {
                            errorMessages.innerHTML = '<p style="color: red; font-weight: bold;">Date cannot be less than 2000.</p>';
                            event.preventDefault();
                        }
                    }
                }
            }
        });
        </script>


