# Codestates Project2 _ TEAM 1
TEAM 1 member : AI_09_장원서, AI_09_이기하, AI_09_정다운

# Semantic Textual Similarity (STS)
## Project Target
- 두 개의 한국어 문장을 입력받아 두 문장의 의미적 유사도 출력
- regression task ( 0 ≤ target ≤ 5)
- FAST API 웹 프레임워크를 사용하여 두 문장의 유사도 점수 출력하는 Server side Code

## Trained Datasets
· KLUE-STS
   - AirBnB (review)
   - Policy (news)
   - paraKQC (스마트홈 쿼리)
 
· KorSTS
   - STS-B dataset
## Process
1. Data EDA (exploratory data analysis)
2. Data Preprocessing
   - Stacking Data
   - cleaning
   - Py-hanspell
3. Pre-trained model 선정; 불러오기
   - KLUE-RoBERTa-base
4. Fine-tuning
5. Hyper-parameter search
   - Wandb
6. Data augmentation
7. Evalation Metirc
   - Pearson'r , f1 socre

**For more detail information, please check report.pdf**

## Dev set score
Pearson's : 92.36, f1 score : 86.01
## Flask
### Model used
   - KLUE-RoBERTa-base

### Preview
![API](https://user-images.githubusercontent.com/94291960/171777506-7cf2aade-2c1a-4568-a80d-7d8b8995e3d2.gif)
