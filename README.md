# Linear-Regression-Model-to-predict-the-Price-of-Houses

###Project Description

<p>The aim of the project to predict the price of houses from the given inputs using a Linear reggression model.</p>

###Format of data set
<p>The input file <a href="https://github.com/NandanNayak/Linear-Regression-Model-to-predict-the-Price-of-Houses/blob/master/ex1data2.txt">ex1data2.txt</a> contains a training set of housing prices in Portland, Oregon. The first column is the size of the house (in square feet), the second column is the number of bedrooms, and the third column is the price of the house. </p>

###Algorithm Description
<p>
<ol>
<li>Since the features vary by orders of magnitude, the featues are normalized so that the Gradiant Descent can minimize quickly. To normalize the feature, the mean value is subtracted from the feature and then divided by standard deviation.</li>
<li>The Gradiant Descent is implemented as a second step. The cost function 'J' is parameterized by theta. In each iteration the values of theta changes based on the gradiant descent equation given below.</li>
<img src="https://github.com/NandanNayak/Linear-Regression-Model-to-predict-the-Price-of-Houses/blob/master/GradiantDescentEqn.png" align="center" />
<li>The cost function is calculated which is expected to reduce with each iteration. The formula is given as below.</li> 
<img src="https://github.com/NandanNayak/Linear-Regression-Model-to-predict-the-Price-of-Houses/blob/master/CostFunctionEqn.png" align="center" />
<li>The optimum values for theta achieved using Gradient descent is verified by the Normal equation which is given as below.</li>
<img src="https://github.com/NandanNayak/Linear-Regression-Model-to-predict-the-Price-of-Houses/blob/master/Normal%20Equation.png" align="center">
</ol>
</p>

###Running the code
<strong><em>python LinearRegressionMultipleVariables.py</em></strong>

###Program Output
The program outputs the model parameters calculated from both the Gradiant Descent equation and Normal equation. The values calculated from the Gradient Descent are approximately equal to those obtained from Normal Equation.
<img src="https://github.com/NandanNayak/Linear-Regression-Model-to-predict-the-Price-of-Houses/blob/edits/Output.png" align="center"/>

###Visualization and Conclusion
<img src="https://github.com/NandanNayak/Linear-Regression-Model-to-predict-the-Price-of-Houses/blob/master/Visualization.png" align="center">
<p>The above plots depict the data points related to <em>Size of House</em> and <em>No. of bedrooms</em> with respect to the <em>Price of house</em>. The Linear regression plot which is the parameterised hypothesis optimized using Gradient Descent is also plotted against the data set to get a better understanding of the Model with respect to the dataset. The Linear regression is not an exact straight line as seen from the plot. This is because the the Model parameters are optimized to values close to a staright line but not exactly a staright line due to the distribution of points in dataset. </p>

<img src="https://github.com/NandanNayak/Linear-Regression-Model-to-predict-the-Price-of-Houses/blob/master/CostFunctionVariation.png" align="center">
<p>The above graph shows the variation of the cost function 'J' with respect to the no. of iterations. As expected the cost function is expected to decrease with the iterations as the Model parameters 'theta' approach the optimum values.</p>

