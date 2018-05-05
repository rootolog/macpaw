def application(env, start_response):
    output = "<html><body><p>Hello. My name is Volodymyr.</p><p>I decided to become a DevOps engineer, so drew attention to the offer of internships in MacPaw.</p><p>I have experience as an technical support engineer, system administrator and ITSM consultant. I have certificates ITIL and MOF. I studied at Web Academy on courses  `Architecting on Amazon AWS` and `DevOps for System Administrator`.</p><p>Thank you for the chance to take an internship. For me, this would be a great opportunity to improve my knowledge by performing the tasks of real work processes, as well as deeper understand the practice of software development. Also I hope that MacPaw will keep in mind my candidacy if appears DevOps engineer vacancy.</p><p>Best regards,<br>Volodymyr</p><p>grep status=401 /var/log/nginx/old.log | wc -l<br>grep remote_addr=8.8.8.8 /var/log/nginx/old.log | wc -l<br>curl --dump-header header hint.macpaw.io<br>ETag `51f33b1cd666a77916ca18d3a913ff58`<br>401+790+51=1242<br>unzip -P 1242 /tmp/additional.zip<br>cat internship-additional<br>This is an additional part of our quest...</p></body></html>".encode('utf-8')
    start_response('200 OK', [
        ('Content-Type', 'text/html; charset=utf-8'),
        ('Content-Length', str(len(output)))
    ])
    return [output]
