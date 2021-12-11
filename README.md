<h1 align="center">Mail Processer</h1>

<div style="margin-left:15px">

<h2>Description</h2>
The application to send out marketing email to its potential customers. 

<br />

<h2>Installation Instruction</h2>
<div style="margin-left:20px">
<h3>Docker</h3>
<div style="margin-left:30px">
To run the program you need some tools & library like:
 - pip3

Step by step:
- Install Docker and run it. <pre>https://docs.docker.com/get-docker</pre> 

- Install Docker Compose via command: <pre> pip3 install docker-compose </pre>

- Run the program via command: <pre> docker-compose up </pre>

</div>
</div>

<div style="margin-left:20px">
<h3>Without Docker</h3>
<div style="margin-left:30px">
To run the program you need some tools & library like:

 - python3.x
 - pip3
 - jinja2
 - pytest
 - freezegun

Run the program via command: 
<pre> python3 send_email.py 
        /path/to/email_template.json 
        /path/to/customers.csv 
        /path/to/output_emails/ 
        /path/to/errors.csv 
</pre>

</div>
Go to output_email.json and errors.csv to see the results.
</div>

<h2>Usage</h2>

</div>