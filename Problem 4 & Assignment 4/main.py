from DataClean import *

def main():
	Name, Biography = dataclean("Sample.txt","stopwords2.txt")
	matrix, whole = matrix_construct(Biography, "frequency")
	bestmatches = kmeans(matrix, 100, cosine, 4)
	Group(bestmatches, matrix, whole, Name, 'output.txt')

if __name__ == '__main__':
	main()