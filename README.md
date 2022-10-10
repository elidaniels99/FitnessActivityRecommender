# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 4: Group Project

## The work

For this project, you will be doing work that focuses on social impact.

The prompts are there to help jump-start your ideation process. If you would like to change or combine prompts, that's fine! If you want to find your own idea, even better. **Consult your instructors for final approval before getting started.**  

Remember to start with a good problem statement!

## The Data

Some prompts have links to data sources, some don't. It's your responsibility to gather and clean your data. For most projects, this will be the bulk of your work.  Start early!

Inspiration for several prompts came from [Data is Plural](https://tinyletter.com/data-is-plural).

## Prompts

### Aviation Accidents

The National Transportation Safety Board (NTSB) [tracks](https://www.ntsb.gov/_layouts/ntsb.aviation/index.aspx) all civilian aviation accidents (and "incidents") going back to 1962.

### Center for Disease Control

The Center for Disease Control has several datasets:
- [Vaccinations](https://data.cdc.gov/browse?category=Vaccinations)
- [Smoking and Tobacco Use](https://data.cdc.gov/browse?category=Smoking+%26+Tobacco+Use)
- [COVID-19](https://data.cdc.gov/browse?tags=covid-19)

### Economic Data

If you're interested in a project focused on the economy, the Bureau of Labor Statistics (BLS) has [several datasets](https://www.bls.gov/data/) ranging from employment to inflation.

### Voter Fraud (or lack thereof)
The Brookings Institute had an [interesting article](https://www.brookings.edu/blog/fixgov/2020/06/02/low-rates-of-fraud-in-vote-by-mail-states-show-the-benefits-outweigh-the-risks/) on voter fraud. Although no datasets are provided, there are several links to sources where you might be able to find some.

### Incarceration

The United States Sentencing Commission (USSC) has [data](https://www.ussc.gov/research/datafiles/commission-datafiles) on federal sentencing going back to 2002.

### Environment

The EPA has data on [air quality](https://cfpub.epa.gov/airnow/index.cfm?action=airnow.main), [precipitation](https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid={BDD5DD12-4942-41A6-B47D-9C2459F28A0A}), [stream flows](https://edg.epa.gov/metadata/catalog/search/resource/details.page?uuid={0599E344-4682-479D-9334-78FE576E2881}) [and more](https://edg.epa.gov/metadata/catalog/main/home.page).

### Protests

[The Mass Mobilization Project](https://massmobilization.github.io/) provides data on demonstrations worldwide, as well as the government responses.

### Charity

[Data.world](https://data.world/datasets/charity) has several datasets related to altruism: donations, organizations, and volunteerism. 

### CTE

Chronic Traumatic Encephalopathy (CTE) is a horrific brain disease, and occurs [frequently](http://www.bu.edu/articles/2017/cte-former-nfl-players/) in former NFL players. Gathering the data will take some work, but here are some starter links.
- [Kaggle](https://www.kaggle.com/jpmiller/nfl-competition-data)
- [Twelve Years of National Football League Concussion Data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3438866/)

### Politics
FiveThiryEight is a great news and commentary site for all things data. Their main foci are sports and politics. If you're interested in polling data, check out the "Data" links in the footer on [this page](https://projects.fivethirtyeight.com/2020-election-forecast/).

### Consumer Complaints

The Consumer Financial Protection Bureau maintains a [dataset](https://www.consumerfinance.gov/data-research/consumer-complaints/) on customer complaints to various financial organizations in the US.

### Professional Athletes

For this prompt, choose a professional sport and compare the distribution of birth months vs the US population. [Sports Reference](https://www.sports-reference.com/) is a good resource for men's and women's sports.

h/t [Malcolm Gladwell](https://youtu.be/kspphGOjApk?t=148)

### SEC

The Securities and Exchange Commission (SEC) is the go-to for [financial data](https://www.sec.gov/edgar/searchedgar/companysearch.html) on US publicly traded companies. The also have [press releases](https://www.sec.gov/litigation/litreleases.shtml) that pertain to various violations.

### US Treasury

The US Treasury Department has several datasets related to public debt. The [yield curve](https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/textview.aspx?data=yield) is a key indicator of economic health. They also maintain data on the sale of [securities](https://www.treasurydirect.gov/instit/annceresult/annceresult.htm).

They also have [auction data](https://home.treasury.gov/services/treasury-auctions) for items that are seized by the IRS.

### Federal Reserve

The Fed has a wide variety of [datasets](https://www.federalreserve.gov/datadownload/) related to the economy and financial markets.

### Still stuck?

Check out [/r/dataisbeautiful](https://www.reddit.com/r/dataisbeautiful/), [Data.world](https://data.world/) and [Kaggle](https://www.kaggle.com/datasets) for inspiration.

## Requirements
This project will be hosted on **GitHib**, not just GA's GitHub Enterprise, so it will be a public project for your portfolio and will add to your github activity.  For the purposes of a DSI project, you must meet a few technical requirements. They are:
1)  A `README.md` file in your project repo. Note that `README` files are automatically rendered by GitHub when you view a repo. Your README should contain:
    - A problem statement.
    - A succinct formulation of the question your analysis seeks to answer.
    - A table of contents, which should indicate which notebook or scripts a stakeholder should start with, and a link to an **executive summary**.
    - A paragraph description of the data you used, plus your data acquisition, ingestion, and cleaning steps.
    - A short description of software requirements (e.g., `Pandas`, `Scikit-learn`) required by your analysis.

2) Your notebook(s) should be **reproducible** and **error-free**. This means:
    - You should set a random seed at the start of every notebook. This will ensure that the random numbers generated in your notebook will be the same every time.
    - You need to provide a _relative path_ to your data, so that if I clone your repo to my machine I can run everything in your repo without error. (You also provide links to any publicly accessible data.)
    - I should be able to `Restart & Run All` in your notebook(s) and see that the _exact same_ results are reproduced.
    - To check that everything worked properly, you may consider forking your own repo to a different location on your computer and checking that all notebooks can run properly from top to bottom.

3) Bear in mind that the value you provide may come from data ingestion, data cleaning, EDA, and/ or a dashboard, etc. While a model may not be immediately apparent, be creative. *Without us telling you exactly what model to build, how could you build a model to increase performance or generate better insights when answering the problem you are facing?*

**Questions**: Questions should be sent to your instructors. **Questions should be specific, brief, and formatted.**
> This is a good practice to develop! When contacting a boss or a client, you should make your question as easy as possible to answer. Consider the following two examples:

> Example 1: "Hey, I have a question. I'm writing a blog post about TensorFlow but got stuck. This part was confusing: https://www.tensorflow.org/api_docs/python/tf/tanh Can you help?"

> Example 2: "The TensorFlow tanh documentation says 'Computes hyperbolic tangent of x element-wise.' What does hyperbolic tangent mean? The link to see more is: https://www.tensorflow.org/api_docs/python/tf/tanh"

> The first example spends about 20 words before mentioning what is going on. The question "Can you help?" is unspecific. The boss/client is required to go to a link in order to get any information about the problem.

> The second example quickly calls out 'Tensorflow tanh documentation,' the explicit quote that is confusing, the explicit question being asked, and a link for additional context. Both examples attempt to get the boss/client/whomever to explain hyperbolic tangent, but imagine how much more quickly someone could answer the second query than the first.

> A helpful way to consider this: When you ask a question, you are basically asking for a favor. You're asking a person to give their time, their brainpower, and their knowledge to you. Every time you ask them to hunt around for more (i.e. they _have_ to travel to a link to get context or they struggle to understand the question you're asking), you're asking a bigger and bigger favor from them.

---

### Teams

Your instructors will divide your class into teams based on interests. Chat with them to find out more!

---

### Presentations

Each group will present their findings.

Your presentation must include:
- A summary of the problem you tackled.
- A walkthrough of how you set out to solve the problem.
- A demonstration of your solution. (i.e. You may demonstrate an app you developed, an example of how a model may be used, etc.)
- A summary of any models you fit and, if applicable, their performance.
- A brief discussion of limitations to your process. (i.e. data collection issues, missing values)
- A brief discussion of next steps.

Presentation requirements:
- *Consider the audience!*
- *As with presentations in the "real world," there is no required time limit.* Your presentation should be long enough to cover all relevant aspects of the problem, but not so long that it obscures the takeaways of the presentation. (Your group should likely aim for somewhere between 15 and 20 minutes, but it is possible that you may need a different amount of time for your presentation.)
- Your presentation must include slides. (Google Slides, PowerPoint, Keynote, etc.)
- Use visuals that are appropriately scaled and interpretable.
- Make sure you provide clear conclusions/recommendations that follow logically from your analyses and narrative and answer your data science problem.

---

### Consulting Project Feedback + Evaluation

Data science is a field in which we apply data to solve real-world problems. Therefore, projects and presentations are means by which we can assess your ability to solve real-world problems in a data-driven manner.

When evaluating projects, there are four areas on which your instructors focus.
1. **Project Requirements: Did you meet all project requirements?** In answering this question, your instructors want to assess how well you met the project requirements as established. These will generally be laid out in the project readme.

2. **Audience: Is your presentation appropriate for the stakeholder?** In answering this question, your instructors want to assess how well you present your results to stakeholders. For example:
  - Did you frame the problem appropriately for the audience?
  - Did you use the appropriate level of technical language for your audience?
  - Did you effectively use your time, or did you encounter an issue such as going significantly beyond or under the allotted time or rushing to conclude the presentation in the allotted time?
  - Did you present effectively, or were there things that detract from the overall presentation such as not speaking loudly enough for the audience or repeating oneself?

3. **Methods: Are your methods appropriate for solving the problem?** In answering this question, your instructors want to assess how well you have applied data science methodology to the problem at hand. For example:
  - Did you make well-reasoned modeling choices, or is there clear evidence that the model is inadequate or improper?
  - Are you able to clearly defend your methodological decisions and results?
  - Did you generalize your results properly, or were your conclusions/inferences improper or fallacious?

4. **Value: Have you provided value to the stakeholder through clear, data-driven recommendations?** In answering this question, your instructors want to assess the value you provide to the stakeholder as a data scientist. For example:
  - Did you answer the problem posed to you?
  - Did you make your recommendations clear, or were the recommendations unclear?
  - Were your recommendations data-driven and based on the results of your work?

You will earn a score for each of the four areas mentioned above.
1. Project Requirements: You may earn a score of 0 or 1. You will earn a score of 1 if all project requirements are met. Otherwise, you will earn a score of 0.
2. Audience: You may earn a score between 0 and 3. A score of 0 indicates that your presentation is inappropriate for the stakeholder. A score of 1 indicates that at least part of your presentation should be non-trivially reworked to be more appropriate for the stakeholder. A score of 2 indicates that there are few to no areas of your presentation that should be reworked. A score of 3 indicates that your presentation is consistently appropriate for the stakeholder and serves as a model for future presentations.
3. Methods: You may earn a score between 0 and 3. A score of 0 indicates that your methods are inappropriate. A score of 1 indicates that your methods are somewhat inappropriate, that justification for methodological decisions is lacking, and/or that your conclusions do not follow from the methods. A score of 2 indicates that your methods are appropriate, justification is sufficient/strong, and your conclusions follow well from the methods. A score of 3 indicates that your methods are excellent, strongly defended, and serves model for future presentations.
4. Value: You may earn a score between 0 and 3. A score of 0 indicates that you provide little to no value to the stakeholder. A score of 1 indicates that the value you provide to the stakeholder is substantially less than expected by not answering the problem, not providing clear recommendations to the stakeholder, and/or providing recommendations that were not data-driven. A score of 2 indicates that the value you provide to the stakeholder is on par with the expectation of providing clear, data-driven recommendations that directly answer the problem posed. A score of 3 indicates that the value you provide to the stakeholder is beyond what is expected and serves as a model for future presentations.

Your final grade will be calculated as follows:
- If any project requirement is not met, the final grade is 'Fail' with a score of 0.
- If all project requirements are met, then the final grade is 'Pass' with a score calculated by summing the above scores. Therefore, if all project requirements are met, the final score will be between a 1 and 10.
