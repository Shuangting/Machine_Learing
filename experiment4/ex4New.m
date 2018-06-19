clear all;
clc;

%% load data
f=fopen('iris.data.txt');
orig=textscan(f,'%f%f%f%f%s','delimiter',',');
fclose(f);

%% data processing
% use numbers to replace properties
% in matirc B, Iris-setosa-->1,Iris-versicolor-->2,Iris-virginica-->3
attributes=[orig{1,1},orig{1,2},orig{1,3},orig{1,4}];
Class=zeros(150,1);
Class(strcmp(orig{1,5},'Iris-setosa')) = 1/3;
Class(strcmp(orig{1,5},'Iris-versicolor')) = 2/3;
Class(strcmp(orig{1,5},'Iris-virginica')) = 1;
data=[attributes Class];
rowrank = randperm(size(Class,1));
data = data(rowrank,:);  % Randomize
data_p=data;
data_p(:,5)=data_p(:,5).*3;
train_data = data(1:120,:);  % Training set & Testing set
test_data = data(121:150,:);
train_datap = data_p(1:120,:);
test_datap = data_p(121:150,:);

%% initializing
r=0.1;   %learning rate
inputNeuron=4;
hiddenNeuron=3;
outputNeuron=1;
iteration = 100000;   % Number of iteration
v0=rand(hiddenNeuron,inputNeuron);  %generating random weight
w0=rand(outputNeuron,hiddenNeuron); 
gamma=rand(hiddenNeuron,1); 
theta=rand(outputNeuron,1); 
v=[v0 gamma];
w=[w0 theta];

%% train&test
[w,v] = trainBP(w,v,train_data,iteration,r);
[accuracy_t]=testBP(w,v,test_data);

%% The Condition of Using Perceptron
theta1 = 0.1;
[transmatrix1 transmatrix2 num] = perceptron1(train_datap,theta1)
right_rate = testperc(transmatrix1,transmatrix2,test_datap)

%% auto encoder
r_e=0.1;   %learning rate
inputNeuron_e=4;
hiddenNeuron_e=3;
outputNeuron_e=4;
iteration_e = 1000;   % Number of iteration
v0_e=rand(hiddenNeuron_e,inputNeuron_e);  %generating random weight
w0_e=rand(outputNeuron_e,hiddenNeuron_e); 
gamma_e=rand(hiddenNeuron_e,1); 
theta_e=rand(outputNeuron_e,1); 
v_e=[v0 gamma];
w_e=[w0 theta];
% train&test
[wAE,vAE] = trainAE(w_e,v_e,train_data,iteration_e,r);
[output,accuracyAE_t]=testAE(wAE,vAE,test_data);

