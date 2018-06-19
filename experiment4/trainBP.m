%% train BP
function [w,v] = trainBP(w,v,train_data,iteration,r)
for j=1:iteration
for i=1:120
    x=train_data(i,1:4);
    X=[x -1]'; 
    yReal=train_data(i,5);
    b0=v*X;   %each neuron value in hidden layer
    b0=1./(1+exp(-b0));  %sigmoid
    b=[b0;-1];  %b is hidden layer
    Y=w*b;
    O=1./(1+exp(-Y));
    g=O.*(1-O).*(yReal-O);
    %updating parameters
    dw=r.*(g*b');
    w=w+dw;
    we=w;
    S=size(dw(1,:));
    we(:,S(1,2))=[];
    e=b0.*(1-b0).*(we'*g);
    %updating parameters
    dv=r.*(e*X');
    v=v+dv;
end
end
end
