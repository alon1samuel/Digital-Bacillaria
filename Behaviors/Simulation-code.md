### Simulation run in SciLab 6.0

#### Simulation of three-cell colony (two interacting pairs)

```python3
x = sin([0:0.01:2*%pi]); // single cycle of a sine wave.  
x = sin([0:0.01:2*8*%pi]); // 8 cycles of a sine wave.  

```
in general, 0:0.01:n is equivalent to n/2*%pi. // restatement of Nyquist theorem.  

```python3

n = length(x); // where n = 629.  
m = n * 0.75 // three-quarter phase resampling (90 degrees out of phase).  
y1 = x(:,n+1:m);  
y2 = x(:,1:n);   
y = cat(2,y1,y2);  
plot(x)  
plot(y)  
```

<p align="center">
  <img src="out-of-phase-quarter-phase-75.png" alt="out-of-phase-quarter-phase-75" height="400" width="500" />
</p>

```python3
n = length(x); // where n = 629.  
m = n * 0.50 // half-phase resampling (180 degrees out of phase).  
y1 = x(:,n+1:m);  
y2 = x(:,1:n);   
y = cat(2,y1,y2);  
plot(x)  
plot(y)  


n = length(x); // where n = 629.  
m = n * 0.25 // one-quarter phase resampling (90 degrees out of phase).  
y1 = x(:,n+1:m);  
y2 = x(:,1:n);   
y = cat(2,y1,y2);  
plot(x)  
plot(y)  
```

<p align="center">
  <img src="out-of-phase-quarter-phase-25.png" alt="out-of-phase-quarter-phase-25" height="400" width="500" />
</p>

#### Extension of cell pair (tangent from an oscillation)

```python3
n = length(x); // where n = 629.  
m = find(x > 0.999999); // three-quarter phase resampling (90 degrees out of phase). Output should be value for array value (1:158).
y11 = n-m+1;  
y1 = ones(1,y11);  
y2 = x(:,1:n);   
y = cat(2,y2,y1);  
plot(x)  
plot(y)  
```

<p align="center">
  <img src="tangent-at-positive-1.png" alt="tangent-at-positive-1" height="400" width="500" />
</p>

```python3
n = length(x); // where n = 629.  
m = find(x == 0); // half-phase resampling (180 degrees out of phase).  
y11 = n-m+1;  
y1 = ones(1,y11);  
y2 = x(:,1:n);   
y = cat(2,y2,y1);  
plot(x)  
plot(y)  


n = length(x); // where n = 629.  
m = find(x , -0.99999); // one-quarter phase resampling (90 degrees out of phase). Output should be value for array value (1:472).
y11 = n-m+1;  
y1 = ones(1,y11);  
y2 = x(:,1:n);   
y = cat(2,y2,y1);  
plot(x)  
plot(y)  
```

<p align="center">
  <img src="tangent-at-negative-1.png" alt="tangent-at-negative-1" height="400" width="500" />
</p>


#### Simulating a noisy sine wave cycle

```python3
rand('seed',0); // reseed with different number every run
x = sin([0:0.01:2*%pi]);
z = rand(1:629);
zz = x .* z;
plot(zz)
```
<p align="center">
  <img src="noisy-sine-wave-sample.png" alt="noisy-sine-wave-sample" height="400" width="500" />
</p>
