# NSD Eucleadian Resemblance

Using Vgg19 to extract feature vectors out of the convolutional layer, we check if the distnce between the two feature vectors
with the same content are closer than two feature vectors with different content.

### Installing

copy this lines to your terminal (with mkl installed):

```
git clone https://github.com/yarinbar/nsd_eucleadian_resemblance
cd nsd_eucleadian_resemblance.git
chmod 777 setup.sh
./setup.sh
```

### Prerequisites

tensorflow version 2.0
keras


## Running the tests

Simply run the command:

```
make test
```

We have 4 tests to test the correctness of the code:
	* euclidean zero vector -> needs to output 0
	* sad (sum of absolute differences) zero vector -> needs to output 0
	* euclidean test -> checks the correctness of the calculations using numpy as ground truth
	* sad test -> checks the correctness of the calculations using numpy as ground truth



## Built With

* [Tensorflow](https://www.tensorflow.org/api_docs) 		- The underlying model framework
* [MKL](https://software.intel.com/en-us/mkl/documentation/view-all) 		- For benchmarking
* [Keras](https://keras.io/) 		- VGG19


## Authors

* **Yarin Bar** - Technion | Israel Institute of Technology


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


