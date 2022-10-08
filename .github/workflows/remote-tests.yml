name: Tests
on: [push]
jobs:
  name: remote ssh command
  build:
    name: Tests
    runs-on: ubuntu-latest
    steps:
    - name: executing remote ssh commands using password
      uses: appleboy/ssh-action@master
      with:
        host: ${{ secrets.HOST }}
        username: ${{ secrets.USER }}
        key: ${{ secrets.KEY }}
        port: ${{ secrets.PORT }}
        script: "cd hackathon202210/metrics && ./start.sh"
