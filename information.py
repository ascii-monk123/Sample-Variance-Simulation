import streamlit as st
from PIL import Image

def app():
    st.title("Why do we divide by (n-1) to calculate the sample variance ?")
    st.text("\n")
    st.text("\n")
    st.header("What is variance ?")
    st.text("\n")
    st.text(" Now first let's get a basic idea about the statistical term ''variance''? What actually is\n variance ? Variance is a statistical term which determines how much spread our data is\n around a central tendency.High variance in a sense means that our data is far away\n from the central tendency and low variance on the other hand means that our data is\n close to the central tendency.")
    st.text("The formula to calculate the variance of an entire population is given below:")
    st.latex(r"\sigma^2 = \frac{\sum_{i=1}^{n}(x_i - \mu)^2} {n}")
    st.text("\n")
    st.header("Visual interpretation of variance")
    st.text(" Now let us visually understand what variance is. Given below are two dot plots which\n represent two different types of distributions."
    )
    st.text("\n")
    less_var=Image.open('./images/less_var.png')
    st.image(less_var,use_column_width=True)
    st.text("\n")
    more_var=Image.open('./images/more_var.png')
    st.image(more_var,use_column_width=True)
    st.text("\n")
    st.text(" Now from the first image, we can see that the distribution is more clustered as compared\n to the second image. The mean of both the images is roughly around 8, but the\n first image has less variance as compared to the second image, as the datapoints in the\n first image are much more closer to the mean as compared to the data points in the second\n image. Even if we calculate the variance using the above given formula, we will find\n that the second image does infact has more variance as compared to the first image.")
    st.text('\n')
    st.header("Population Variance vs Sample Variance.")
    st.text("\n")
    st.text(" Now, we have a basic idea about what variance is. So, let's talk about\n population and sample variance.")
    htmlString='''
    <p style="font-size:14px;"><b>Population Variance:</b> Population variance is the variance value that we compute for the entire
    statistical population under consideration. It gives us an unbiased estimate about the spread of the data around
    a central tendency. The formula for population variance is already given above.</p>
    '''
    st.markdown(htmlString,unsafe_allow_html=True)
    htmlString2='''
    <p style="font-size:14px;"><b>Sample Variance:</b> Now, it's sometimes impossible for us to collect the data related to an entire population (for
    logic let's say the entire age data of all the boys in the world). Now, in order to find a central value, let's say the average age,
    we have to take a subset from the entire population, calculate the average  and then infer it for the entire population. This is inferential statistics.
    We won't be discussing that here, as it's a vast discpline and discussing about it is not our aim to begin with.</p>
    <p style="font-size:14px;">So, what is sample variance? It's easy!! The variance that we calculate from the subset of a population in order to infer to the whole population, is called sample variance. &#128512;<br/>
    The formula for sample variance is given below.</p>

    '''
    st.markdown(htmlString2,unsafe_allow_html=True)
    st.latex(r"S^2 = \frac{\sum_{i=1}^{n}(x_i - \overline{x})^2} {n-1}")
    st.text(' Hey wait a minute?? Why are we dividing by n-1 to calculate the sample variance.\n Isn\'t it supposed to be n??')
    st.markdown('''&#128517;&#128517; ''',unsafe_allow_html=True)
    st.header("Demystifying the sample variance formula :)")
    st.text(" For understanding the intution behind the sample variance formula, we will use the\n help of the figure given below.")
    graph=Image.open('./images/simulation.png')
    st.image(graph,use_column_width=True)
    st.text('\n')
    st.text("The above graph plots the relation between average sample variance/population\n variance for various sample sizes. In short what the simulation does is that, it iterates\n n times and for each iteration, it generates a random sample of size between 0 to 10.\n After that, it calculates the ratio of the sample's variance to that of the population\n variance and then averages it. It's best to allow the simulation to iterate\n at least 1000 times so that the information can be generalized better, as we\n have a large range of ratios to take the average of.")
    htmlText='''
    <p style="font-size:13px;letter-spacing:1px;">Now,as we can see that for sample size=2, the ratio of sample variance and population 
    variance is roughly about 50 percent on an average. And as another example, for sample size=3, the ratio of sample
    variance and population variance is around 66 percent on an average.Similarily we can find percentages for n==4,5,... and so on. 
    The conclusion that we reach from the simulation is that for sample size n, the sample variance is (n-1)/n times the population variance.
    You can try the simulation yourself by clicking the simulation radio button on the left side of the page. You can also adjust the simulation parameters 
    by clicking on the parameters button.<br/><br/> <b>Note:</b> Since streamlit generates pages on the fly, it is advised that you scroll to the top after pressing each radio button 
    on the left side. Because by default, streamlit always keeps the scrolling position to the current position of your scroll.
    </p>

    '''
    st.markdown(htmlText,unsafe_allow_html=True)
    st.text('Now we will derive the formula for sample standard deviation')
    st.text('From the logic discussed above, we have :')
    st.latex(r'''
    \frac{(n-1)\sigma^2}{n} = S^2
    ''')
    st.latex(r'''
    \frac{(n-1)\sigma^2}{n} = \frac{\sum_{i=1}^{n}(x_i - \overline{x})^2} {n}
    ''')

    st.latex(r'''
    \sigma^2 = \frac{\sum_{i=1}^{n}(x_i - \overline{x})^2} {n-1}
    ''')

    st.text(' So from the above equation, we can basically infer that by dividing the mean squared\n difference by n-1, we can find the unbiased population variance')
    st.text('\n\n')
    st.text(' So thats it. I hope that you enjoyed learning something new today.\n Don\'t forget to run some simulations too.')
    st.markdown(r'''&#128512; &#128512;''',unsafe_allow_html=True)
    st.text('\n\n\n')
    st.text('Simulation made by aahan singh charak')
    


