from bottle import get, request, route, run

#1:Landing Page
@route('/') #opens home
def Welcome():#creates the landing page
    return """
            <!DOCTYPE html><html><head><style>
            header {background-color:black; color:white;text-align:center; padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px; width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head>
            <body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav>
            <h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section>
            <h1>Welcome</h1>
            <p>If you are like me, you struggle mightely when it comes time to decide what statistical test you should
            run and sites like <a href="http://www.ats.ucla.edu/stat/mult_pkg/whatstat/default.htm"> this<a/>
            don't make it much easier.</p>
            <p>Therefore, in an attempt to simplify the process, this site provides the "Which Test Should I Run?" decision tree
            and <a href="https://www.lucidchart.com/invitations/accept/740e1b43-8806-4b5a-879d-90c57271b582">flow chart<a/>.</p>
            <p>Additionally, please note the example studies are taken from Jennifer Larson-Hall's <a href="http://www.routledgetextbooks.com/textbooks/9781138024571/">
            <i>A Guide to Doing Statistics in Second Language Research Using SPSS and R</i></a>.</p>
            <p>To that end, either select one of the links on the left to read more about each of the common tests in
            Applied Linguistics or press "Next" to start the process of deciding which test to run.

            <form action="/testme">
              <input type="submit" value="Next">
            </form>
            </section>

            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer>

            </body></html>"""

#2:First decision: are you trying to find similarities or differences?
@get('/testme')
def testme():
    return '''
            <!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position:fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>Lets start at the beginning...</h1>
            <p><img style="-webkit-user-select: none" src="http://dirt2doorbell.com/wp-content/uploads/2015/11/soundofmusic-topper-1.jpg"></p>
            <p>Are you trying to find what makes your groups similar or different? </p>


            <form action="/test2" method="get">
              <input type="radio" name="relationships" value="similar" checked > Similar<br>
              <input type="radio" name="relationships" value="different"> Different<br>
              <input type="Submit" value="submit"><br>
            </form>

            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>
            '''

#3: Controlling for Varables
@get('/test2', method="get")
def doTest():
    relationships=request.query.get("relationships")
    if relationships == "similar":
        return """ <!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>What makes us the same?</h1>
            <p>Alright, how many <a href="http://www.abs.gov.au/websitedbs/a3121120.nsf/home/statistical+language+-+what+are+variables/">
            variables<a/> do you have? In other words, how many things are you comparing?</p>

            <form action="/test3" method="get">
              <input type="radio" name="NumberOfVariables" value="exactly two" checked > Exactly Two<br>
              <input type="radio" name="NumberOfVariables" value="more than two"> More Than Two<br>
              <input type="Submit" value="submit"><br>
            </form>

            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>
            """
    else:#This will then start the process for group differences
        return """<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>What makes us unique?</h1>
            <p>Alright, you obviously have more than one <a href="http://www.abs.gov.au/websitedbs/a3121120.nsf/home/statistical+language+-+what+are+variables/">variable<a/>.</p>
            <p>However, are you trying to <a href="http://www.visionlearning.com/en/library/Process-of-Science/49/Controlling-Variables/163/">control<a/> for anything?</p>
            <p>For example, do you want to see if length of education matters when age is controlled for?</p>

            <form action="/test6" method="get">
              <input type="radio" name="Control" value="yes" checked > Yes<br>
              <input type="radio" name="Control" value="no"> No<br>
              <input type="Submit" value="submit"><br>
            </form>

            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>"""

@get('/test3', method="get")
def test3():
        variables=request.query.get("NumberOfVariables")
        if variables=="exactly two":
            return'''<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>Last question. I promise.</h1>
            <p>Good. So tell me a little about the variables: are <b>BOTH</b> of them
            <li><a href="http://stattrek.com/statistics/dictionary.aspx?definition=Categorical%20variable/">categorical<a/>
            meaning they can't be ranked (like colors), or</li>
            <li><a href="http://stattrek.com/statistics/dictionary.aspx?definition=quantitative%20variable/">continuous<a/>?</li></p>

            <form action="/result1" method="get">
              <input type="radio" name="TypeOfVariables" value="Categorical" checked > Categorical<br>
              <input type="radio" name="TypeOfVariables" value="Continuous"> Continuous<br>
              <input type="Submit" value="submit"><br>
            </form>

            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>'''
        else:
            return'''<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position:fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>Tell Me More</h1>
            <p>Do you have a <a href="http://www.statisticshowto.com/dependent-variable-definition/#DVD/">dependent variable</a>?</p>
            <p>It could be:</p>
            <li>scores on a test</li>
            <li>number of words read</li>
            <li>length of pauses</li>
            <p>or anything else that you are measuring.</p>

            <form action="/test4" method="get">
              <input type="radio" name="DependentVariable" value="Yes" checked >Yep<br>
              <input type="radio" name="DependentVariable" value="No">Nope<br>
              <input type="Submit" value="submit"><br>
            </form>

            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>'''

@get('/result1', method="get")
def test3():
    variables=request.query.get("TypeOfVariables")
    if variables=="Categorical": #Chi Square
        return '''<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>Chi Square</h1>
            <p>It looks like a chi square test is in your near future.</p>
            <p>BTW, did you say you were into corpus?</p>
            <p>For example, <a href="http://onlinelibrary.wiley.com/doi/10.1111/j.0023-8333.2006.00342.x/abstract/"> Geeslin and Guijarro-Fuentes (2006)</a>, asked:</p>
            <blockquote cite="http://www.routledgetextbooks.com/textbooks/9781138024571/">
            Will three groups (Spanish L1, Portuguese L1, and Portuguese L1 and Spanish L2) differ in their choice of corpula (<i>ser</i>, <i>estar</i> or both) in a contextual usage measure?
            </blockquote>
            <p>Basically, the authors were trying to find whether group membership affected frequency of use.</p>
            <p>Also, pro tip:</p>
            <p><img style="-webkit-user-select: none" src="http://1.bp.blogspot.com/-kfJwjZwPSOc/Va6AQebMvZI/AAAAAAAAMT4/J0fQCCgi7y0/s400/848767.jpg"></p>
            <p>For further information, see the following video:</p>
            <p><iframe width="560" height="315" src="https://www.youtube.com/embed/43dWGwr9g_k" frameborder="0" allowfullscreen></iframe></p><br><br>
            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>'''
    else:#correlation
        return'''<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>Correlation: Looking for overlap</h1>
            <p>Correlation, according to Larson-Hall (2016), <q>looks at how two measurements vary together.</q></p>
            <p>For example, <a href="http://journals.cambridge.org/action/displayAbstract?fromPage=online&aid=2747404&fileId=S0142716400009863/"> Pearson, Fernandez, Lewedeg, and Oller</a> (1997) asked:</p>
            <blockquote cite="http://www.routledgetextbooks.com/textbooks/9781138024571/">
            Does the amount of input that a bilingual chld receives matter to how much vocabulary they will learnin in Spanish?
            </blockquote>
            <p>Essentially, the authors are trying to find what (if any) is the relationship between the amount of input a bilingual child receives in relation to the amount of Spanish vocabulary the child has learned. </p>
            <p>Also, be sure to remember<p>
            <img style="-webkit-user-select: none" src="https://s-media-cache-ak0.pinimg.com/236x/34/20/fe/3420fe923bdcaf6991361fdbf8b6a785.jpg"></p>
            <p> For a further discussion of the correlational studies, see the short video below. <p><iframe width="560" height="315" src="https://www.youtube.com/embed/4EXNedimDMs" frameborder="0" allowfullscreen></iframe><p/>

            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>'''

@get('/test4', method="get")
def result2():
    DependentVariable=request.query.get("DependentVariable")
    if DependentVariable=="Yes":#Multiple Regression
        return'''<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>Multiple Regression</h1>
            <p><img style="-webkit-user-select: none" src="https://cdn.meme.am/instances/400x/67212057.jpg"></p>
            <p><a href="https://en.wikipedia.org/wiki/Linear_regression#Simple_and_multiple_regression/">Multiple regression <a/> looks at the different relationsips among variables in order to make a prediction about a dependent variable.</p>
            <p>See. Easy, right?<p>
            <p>For example, Zareva (2005) asked</p>
            <blockquote cite="http://www.routledgetextbooks.com/textbooks/9781138024571/">
            To what extenct could self-reported vocabulary knowledge(IV 1), vocabulary size (IV 2), vocabulary difficulty
            (IV 3), native-like associational knowledge (IV 4),and number of assciations made (IV 5) predict an actual measure of vocabulary knowledge(DV)?
            </blockquote>
            <p>As can be seen above, the authors were attempting to find what (if any) was the relationship between the
             vocabulary measures and actual vocabulary knowledge so as to create a framework with <q>the fewest possible
             predictors</q> (Larson-Hall, 2016).</p>
            <p>For a further explanation, see the video below</p>
            <p><iframe width="420" height="315" src="https://www.youtube.com/embed/JXRyCiuL46A" frameborder="0" allowfullscreen></iframe></p><br>
            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>'''
    else:#Partial Correlation
        return'''<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>Partial Correlation</h1>
            <p>Partial-correlation, according to Larson-Hall (2016), <q>looks at how two measurements vary together when a third has been factored out</q></a>.</p>
            <p>Essentially, we want to see how two variable relate to each other once we <a href=http://www.stat.yale.edu/Courses/1997-98/101/expdes.htm/>control</a> for a third variable that we think is getting in the way or that we want to account for.</p>
            <p>For example, <a href="http://las.sagepub.com/content/49/4/521.short/"> Larson-Hall</a> (2006) asked:</p>
            <blockquote cite="http://www.routledgetextbooks.com/textbooks/9781138024571/">
            How does age at which a learner began studying English as a Foreign language relate to scores on a grammaticality judgement test and a phoneme contrast test? Those who began studying earlier might have more total input, so this factor is statistically subracted out of the equation by using partial correlation.
            </blockquote>
            <p>Essentially, the authors are trying to find what (if any) is the relationship between age and test score once the amount of total input is controlled for.</p>
            <p>Also, be sure to remember<p>
            <img style="-webkit-user-select: none" src="https://s-media-cache-ak0.pinimg.com/236x/34/20/fe/3420fe923bdcaf6991361fdbf8b6a785.jpg"></p>
            <p> For a further discussion of partial-correlation studies, see the following short video below. <p><iframe width="420" height="315" src="https://www.youtube.com/embed/ty1owIoev3o" frameborder="0" allowfullscreen></iframe><p/><br>

            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>'''

@get('/test6', method="get")
def test6():
    control=request.query.get("Control")
    if control=="yes":#ANCOVA
        return '''<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>Looks like <a href="http://oak.ucc.nau.edu/rh232/courses/eps625/handouts/ancova/understanding%20ancova.pdf/">ANCOVA</a> for you!</h1>
            <p>ANCOVAs sound complicated but they are relatively straight forward.</p>
            <p>Take this from <a href="http://www.sciencedirect.com/science/article/pii/S016763930500052X/">Dromey, Silveira and Sandor (2005)</a>:</p>
            <blockquote cite="https://www.routledge.com/products/9781315775661">Are there differences between groups with different language backgrounds (three groups) and different gender (two genders) in how accurately they recognize the affect in someone's voice when the participant's age is statiscally controlled for?
            </blockquote>
            <p>As you can see from the example above, care about language backgrounds and gender, but do not want age to affect their measurements.</p>
            <p>Therefore, to measure what they want and factor out the "noise" they control for what they do not.</p>
            <p>Do worry if this sounds confusing. Watch the following video and pay very close attention to the first minute:</p>
            <iframe width="420" height="315" src="https://www.youtube.com/embed/mApbp1RDy-U" frameborder="0" allowfullscreen></iframe>
            <br>
            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>'''
    else:
        return '''<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>We have no control!</h1>
            <p>Ok, so we're not controlling for anything.</p>
            <p>Tell me something: how many variables do you have? Remember, variables can have several levels. What does that mean?</p>
            <p>Take nationality: you could have over a dozen nationalities in your study but nationality would only count as one variable with
            (depending on your categorization) several, or just one, group.</p>
            <p>So, how many variables do you have in your study?</p>
            <form action="/test7" method="get">
              <input type="radio" name="Variables" value="two" checked > Two<br>
              <input type="radio" name="Variables" value="more than two"> More than two<br>
              <input type="Submit" value="submit"><br>
            </form>

            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>'''

@get('/test7', method="get")
def test7():
    variables=request.query.get("Variables")
    if variables=="two":
        return'''<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>Lets talk about your participants</a>!</h1>
            <p>How many groups of participants do you have?</p><p>For example, if your population is divided into experimental group and control, that would be two groups.</p>
            <form action="/test9" method="get">
              <input type="radio" name="Groups" value="Two" checked > Two<br>
              <input type="radio" name="Groups" value="More Than Two"> More than two<br>
              <input type="Submit" value="submit"><br>
            </form>
            <br>
            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>'''
    else:
        return '''<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>We have a plethora of variables</h1>
            <p>Ok, so we're not controlling for anything.</p>
            <p>Also, we have at least three variables but how many of them are <a href="http://examples.yourdictionary.com/independent-and-dependent-variable-examples.html/">independent</a>?</p>
            <form action="/result2" method="get">
              <input type="radio" name="IndependentVariables" value="One" checked > One<br>
              <input type="radio" name="IndependentVariables" value="Two"> Two or more<br>
              <input type="Submit" value="submit"><br>
            </form>

            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>'''

@get('/result2', method="get")
def result2():
    IndependentVariables=request.query.get("IndependentVariables")
    if IndependentVariables=="One":#MANOVA
        return'''<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>It's <a href="http://userwww.sfsu.edu/efc/classes/biol710/manova/MANOVAnewest.pdf/">MANOVA</a> Time!</h1>
            <p>Congratulations! If you are seeing this page it either means:</p>
            <li> you hit the wrong button</li>
            <p>OR</p>
            <li> you have one independent variable and multiple dependent variables.
            <p>In other words, you either made a mistake or you want to see how something like nationality (IV) can affect someone's writing score (DV) and speaking score (DV).</p>
            <p>For a further example, please see this <a href="http://www.statisticallysignificantconsulting.com/Manova-Statistic-SPSS.htm/">link</a>
             but keep in mind that according to Larson-Hall in <i>A Guide to Doing Statistics in Second Language Research Using Spss and R</i>, <q>in the field of second langauge research, few actual MANOVAs are used</q> (p184).</p>
            <iframe width="560" height="315" src="https://www.youtube.com/embed/m0zV_wFGA1I" frameborder="0" allowfullscreen></iframe></c>
            <br>
            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>'''
    else:#Factorial ANOVA
        return'''<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>It's Time for a <a href="http://www.statisticssolutions.com/conduct-interpret-factorial-anova/"> Factorial ANOVA</a>!</h1>
            <p>Welcome to the land of looking for <a href="http://support.minitab.com/en-us/minitab/17/topic-library/modeling-statistics/anova/anova-models/what-is-an-interaction//">interactions</a>!</p>
            <p>In other words, when you have more than one IV, you may find that the affect of the IVs may differ depending on how they are combined (Larson-Hall, 2016).</p>
            <p>For example, <a href="http://slr.sagepub.com/content/21/2/121.short/">Juffs 2005</a>, a <b>two-way ANOVA</b>, asked:</p>
            <blockquote cite="http://www.routledgetextbooks.com/textbooks/9781138024571/">
            Does the L1 of learners from different language backgrounds affect how they process grammatical and ungrammatical wh-extraction in English sentences? Learners from four different L1 backgrounds were tested. Is there any effect for the specific kinds of structures that the wh-word is extracted out of? Three differnt kinds of structures were tested.
            </blockquote>
            <p> To unpack that, there is <b>one dependent variable</b> (grammatical accuracy score) and <b> one independent variable with four levels</b> (the four L1s).</p>
            <p>For example, <a href="http://onlinelibrary.wiley.com/doi/10.1111/j.0023-8333.2006.00343.x/abstract/">Kondo-Brown (2006)</a> a <b>three-way ANOVA</b> asked:</p>
            <blockquote cite="http://www.routledgetextbooks.com/textbooks/9781138024571/">Do groups of readers who differ in their reading proficiency (more proficient versus less proficient) perform differently depending on whether they are guessing the meaning or pronunciation of unknown words, and also depending on whether they see the words in context or in insolation? </blockquote>
            <p>Again, performance on the test is the <b>dependent variable</b>, while the two <b>independent variables</b>, with two levels each, are:</p>
            <ol>
            <li>task: 1) guessing meaning or 2) guessing the pronunciation</li>
            <li>context: 1) words in isolation or 2) words located in context</li>
            </ol>
            <p>Confused? Good because it is confusing.</p>
            <p>If not, good because you are getting this concept down.</p>
            <p>Either way, here is a video that might clear some things up.</p>
            <p><iframe width="560" height="315" src="https://www.youtube.com/embed/q4IJtIzgg_Y" frameborder="0" allowfullscreen></iframe></p>
            <br>

            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>'''

@get('/test9', method="get")
def test9():
    groups=request.query.get("Groups")
    if groups=="Two":
        return '''<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>Testing. 1,2,3,Testing.</h1>
            <p>How many times are you testing these groups?</p>
            <form action="/test11" method="get">
              <input type="radio" name="testing" value="once" checked > Once<br>
              <input type="radio" name="testing" value="twice"> Twice<br>
              <input type="radio" name="testing" value="more"> More than twice<br>
              <input type="Submit" value="submit"><br>
            </form>

            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>'''
    else:#RM-Anova
        return '''<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>Testing. 1,2,3,Testing.</h1>
            <p>How many times are you testing these groups?</p>
            <form action="/test10" method="get">
              <input type="radio" name="testing" value="once" checked > Once<br>
              <input type="radio" name="testing" value="twice"> More than Once<br>
              <input type="Submit" value="submit"><br>
            </form>

            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>'''

@get('/test10', method="get")
def test10():
    testing=request.query.get("testing")
    if testing=="once":#One-way ANOVA
        return '''<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>It's Time for a <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php/"> One-way ANOVA</a>!</h1>
            <p>So you have different groups, but are they statiscally different?</p>
            <p>In order to answer that question, we run a One-way ANOVA <q>to test whether the scores of three or more groups oro lesvels differ statistically</q> (Larson-Hall, 2016).</p>
            <p>For example, <a href="https://www.researchgate.net/publication/228891055_Perceptual_paths_to_accurate_production_of_L2_vowels_The_role_of_individual_differences/">Baker and Trofimovich (2006)</a>, asked:</p>
            <blockquote cite="http://www.routledgetextbooks.com/textbooks/9781138024571/">
            "Does the amount of L2 learners' experience influence their produc tion of L2 suprasegmentals?" (p. 5). Three groups of Korean users or English were distinguished by their length of residence in the USA; L1 speakers of English were also tested.
            </blockquote>
            <p> To unpack that, the question was if the differences in production of suprasegmentals <b>dependent variable</b> between the four groups, the <b>independent variable with four levels</b> (three groups of Korean speakers and onge group of L1 English speakers) was enough to say the groups were different in a statiscally significant way.</p>
            <p>For a further explanation, see the following video:</p>
            <iframe width="560" height="315" src="https://www.youtube.com/embed/0Vj2V2qRU10" frameborder="0" allowfullscreen></iframe>
            <br>
            <br>

            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>'''
    else:#RM-ANOVA
        return '''<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>Take Two, Three, Four, Ect.: <a href="http://www.statisticssolutions.com/conduct-interpret-repeated-measures-anova/">Repeated-measures ANOVA</a>!</h1>
            <p>RM-ANOVA are useful for longitudinal studies where the same groups are measured repeatedly as in the case of:</p>
            <li> pretest, postest and/or delayed posttest socres</li>
            <li> proficiency levels measured after one week, six weeks and 12 weeks</li>
            <li> use of conditionals after three and six months of training</li>
            <p>For example, <a href="http://onlinelibrary.wiley.com/doi/10.1111/j.0023-8333.2006.00349.x/abstract/"> Toth (2006)</a>, asked:</p>
            <blockquote cite="http://www.routledgetextbooks.com/textbooks/9781138024571/">
            Will processing instruction provide any benefits over a cummunicative approach when participants must prductively use Spanish <i>se</i> in a sentence produciton task? There were three groups, who all received differnt tyupes of input. Will there be differences on a delayed posttest (24 days later) as well as an immediate posttest? There was also a pretest, resulting in three different times of testing.
            </blockquote>
            <p>Since there were multiple groups, tested multiple times, a RM-ANOVA was called for.</p>
            <p>For a further explanation, see the following video:</p>
            <iframe width="560" height="315" src="https://www.youtube.com/embed/VPB3xrsFl4o" frameborder="0" allowfullscreen></iframe>
            <br>
            <br>
            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>'''

@get('/test11', method="get")
def test10():
    testing=request.query.get("testing")
    if testing=="once":#Independent Samples t-test
        return '''<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>No pre-test? Looks like it's time for an <a href="http://libguides.library.kent.edu/SPSS/
            IndependentTTest/">Independent Samples t-test</a>!</h1>
            <p>As Urdan( 2010) succintly states a t-test:</p>
            <blockquote cite="http://www.sanghv.com/download/soft/machine%20learning,%20artificial%20intelligence,%20mathematics%20ebooks/math/statistics/statistics%20in%20plain%20english%20(3rd,%202010).pdf/">
            is designed to answer a fairly straightforward question: Do two independent samples differ from each other <i>significantly</i> in their average scores on some variable?
            </blockquote>
            <p>For example, <a href="http://www.tandfonline.com/doi/abs/10.1080/0958822042000319629#.VyuQ97orKcw/"> Hirata (2004)</a>, asked:</p>
            <blockquote cite="http://www.routledgetextbooks.com/textbooks/9781138024571/">
            Do English-speaking learners of Japanese who receive pronunciation training on a computer improve their
             performance on pitch and duration contratst in Japanese more than controls?
            </blockquote>
            <p>Basically, is the difference between the group that participated in CALL activities statistically signifanct from the group that didn't?</p>
            <p>For a further explanation, see the following video:</p>
            <p><iframe width="560" height="315" src="https://www.youtube.com/embed/o-e9I_VbLR8" frameborder="0" allowfullscreen></iframe></p>
            <br>
            <br>
            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>'''
    elif testing=="twice":#Paired Samples t-test
        return '''<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>Have a pre and post test? Time for a <a href="http://libguides.library.kent.edu/SPSS/PairedSamplestTest/">Paired/Dependent Samples t-test</a></h1>
            <p>Larson-Hall in <i>A Guide to Doing Statistics in Second Langauge Research Using SPSS and R</i> states:</p>
            <blockquote cite="https://www.routledge.com/products/9781315775661/">
            A <b>paried samples t-test</b> is used when the people who are tested are the same, so that the two mean scores cannot be independent of each other.
            </blockquote>
            <p>For example, <a href="http://ltr.sagepub.com/content/10/3/297.short/"> Macaro and Masterman (2006)</a>, asked:</p>
            <blockquote cite="http://www.routledgetextbooks.com/textbooks/9781138024571/">
            Would English-speaking students studying French benefit from a short, intensive burst of explicit grammar training in their L2? The students were tested before the trinaing and then after the training?
            </blockquote>
            <p>In essence, the author is trying to decipher whether the group's improvement over time is statistically significant.</p>
            <p>For a further explanation, see the following video:</p>
            <p><iframe width="560" height="315" src="https://www.youtube.com/embed/DzitbJHIBQM" frameborder="0" allowfullscreen></iframe></p>
            <br>
            <br>
            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>'''
    else:#RM ANOVA
        return '''<!DOCTYPE html><html><head><style>
            header {background-color:black;color:white;text-align:center;padding:5px;}
            nav {line-height:30px;background-color:#eeeeee;height:400px;width:200px;float:left;padding:5px;}
            section {width:1000px;float:left;padding:10px;}
            footer {width:1000px;position: fixed;bottom:0px;background-color:black;color:white;clear:both;text-align:center;padding:5px;}
            </style></head><body>

            <header><h1>Common Statistical Tests in Applied Linguistics</h1></header>

            <nav><h3>Test of Relationships</h3>
            <a href="https://en.wikipedia.org/wiki/Correlation_and_dependence">Correlation<a/><br>
            <a href="http://www.linguistics.ucsb.edu/faculty/stgries/research/2012_STG_IndRels_EncApplLing.pdf">Chi Square<a/><br>
            <a href="http://www.statisticssolutions.com/partial-correlation/">Partial Correlation<a/><br>
            <a href="http://www.statsoft.com/Textbook/Multiple-Regression#general">Multiple Regression<a/><br>
            <h3>Test of  Differences</h3>
            <a href="http://researchbasics.education.uconn.edu/t-test/">t-test<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php">ANOVA<a/><br>
            <a href="https://statistics.laerd.com/statistical-guides/repeated-measures-anova-statistical-guide.php">RM-ANOVA<a/><br>
            <a href="http://www.statisticshell.com/docs/ancova.pdf">ANCOVA<a/><br>
            </nav>

            <section><h1>In it for the Long Haul: <a href="http://www.statisticssolutions.com/conduct-interpret-repeated-measures-anova/">Repeated-measures ANOVA</a>!</h1>
            <p>RM-ANOVA are useful for longitudinal studies where the same groups are measured repeatedly as in the case of:</p>
            <li> pretest, postest and delayed posttest scores</li>
            <li> proficiency levels measured after one week, six weeks and 12 weeks</li>
            <li> use of conditionals after three, six and nine months of training</li>
            <p>For example, <a href="http://onlinelibrary.wiley.com/doi/10.1111/j.0023-8333.2006.00349.x/abstract/"> Toth (2006)</a>, asked:</p>
            <blockquote cite="http://www.routledgetextbooks.com/textbooks/9781138024571/">
            Will processing instruction provide any benefits over a communicative approach when participants must prductively use Spanish <i>se</i> in a sentence produciton task? There were three groups, who all received differnt tyupes of input. Will there be differences on a delayed posttest (24 days later) as well as an immediate posttest? There was also a pretest, resulting in three different times of testing.
            </blockquote>
            <p>Since there were multiple groups (but there didn't need to be), tested multiple times, a RM-ANOVA was called for.</p>
            <p>For a further explanation, see the following video:</p>
            <iframe width="560" height="315" src="https://www.youtube.com/embed/VPB3xrsFl4o" frameborder="0" allowfullscreen></iframe>
            <br>
            <br>
            <footer>Copyright © <a href="https://teachinglearninglearningteaching.wordpress.com/">Teaching Learning Learning Teaching</a>
            </footer></body></html>'''

run(host='localhost', port=8080, reloader=True)
