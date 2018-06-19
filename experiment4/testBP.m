%% test BP
function [accuracy_t]=testBP(w,v,test_data)
    wrongNum=0;
for i=1:30
    x=test_data(i,1:4);
    X=[x -1]';
    bTest=v*X;
    bTest=1./(1+exp(-bTest));
    bTest=[bTest;-1];
    yTest=w*bTest;
    yTest=1./(1+exp(-yTest));
    if abs(test_data(i,5)-yTest)>0.15
        wrongNum=wrongNum+1;
    end
end
totalWrong=wrongNum/30;
accuracy_t=1-totalWrong;
