%% test AE
function [out,accuracy_t]=testAE(w,v,test_data)
for i=1:4
    test_dataAE(:,i)=(test_data(:,i)-min(test_data(:,i)))/(max(test_data(:,i))-min(test_data(:,i)));
end
output=[];
wrongNum=0;
for i=1:30
    xt=test_dataAE(i,1:4);
    Xt=[xt -1]';
    bTest=v*Xt;
    bTest=1./(1+exp(-bTest));
    bTest=[bTest;-1];
    yTest=w*bTest;
    yTest=1./(1+exp(-yTest));
    if((abs(test_data(i,1:4)'-yTest))>0.2)
        wrongNum=+1;
    end
    output(i,:)=yTest;
end
totalWrong=wrongNum/30;
accuracy_t=1-totalWrong;
for i=1:4
    out(:,i)=(max(test_data(:,i))-min(test_data(:,i))).*output(:,i)+min(test_data(:,i));
end
end
