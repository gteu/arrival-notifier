# arrival-notifier

```
aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin [your aws id].dkr.ecr.ap-northeast-1.amazonaws.com
aws ecr create-repository --repository-name arrival-notifier --region ap-northeast-1
docker tag selenium/standalone-chrome:4.0.0-rc-3-20211010 [your aws id].dkr.ecr.ap-northeast-1.amazonaws.com/arrival-notifier:selenium-chrome
docker push [your aws id].dkr.ecr.ap-northeast-1.amazonaws.com/arrival-notifier:selenium-chrome
```
