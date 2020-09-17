docker build -t juankanh/myimagenpyhton .
docker run -d -p 5000:5000 juankanh/myimagenpyhton
docker exec -it dc096e15aba194b8255601c81a224b946f10319539aaea4237b6a66787725a0b /bin/sh -c "[ -e /bin/bash ] && /bin/bash || /bin/sh"