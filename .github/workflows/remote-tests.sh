name: Tests

on:
  schedule:
  - cron: "0 4 * * *" # everyday at 4 am
  push:
    branches:
      - master
    # Publish `v1.2.3` tags as releases.
    tags:
      - v*

  # Run tests for any PRs.
  pull_request:

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
