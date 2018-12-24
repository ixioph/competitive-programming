#Program to simplify expressions

#algorithm
# Scan the string, by each character
# If the first character is not a (-) place (+) into the buffer
# Place each character into a temporary buffer
# If you encounter a letter with no preceding integer, insert a "1"
# If you encounter a (-) or (+), save the contents of the buffer and clear it for the next monomial
###
# Split the Monomial into the coefficient and the literal
# Sort the literal alphabetically for easy comparisons and by number of variables
# Add together the coefficients for each literal
###
# Append the final coefficient to the front of its corresponding literal
# Arrange these terms in order lexicographically and by increasing number of variables in the literal
# Remove any leading (+) or coefficient of 1 and merge these terms into one new string expression
# Return the created string 
