# Automatic Theorem Proofs 

## Geometry of interaction
 

## Functional Analysis Theorems: 

1. **Riesz Representation Theorem**:
$\forall f \in \mathcal{H}', \exists y \in \mathcal{H} \text{ such that } f(x) = \langle x, y \rangle \text{ for all } x \in \mathcal{H}$

2. **Open Mapping Theorem (Banach-Steinhaus Theorem)**:
   $\text{If } T:X \to Y \text{ is a bounded linear operator between Banach spaces, then } T(X) \text{ is open in } Y$

3. **Closed Graph Theorem**:
   $\text{A linear operator } T:X \to Y \text{ between Banach spaces is closed if and only if its graph } \{(x, Tx) \mid x \in X\} \text{ is closed in } X \times Y.$

4. **Hahn-Banach Theorem**:
   $\text{For any subspace } Y \subset X \text{ and any linear functional } f_0 : Y \to \mathbb{K}, \text{ there exists an extension } f : X \to \mathbb{K} \text{ such that } f|_Y = f_0 \text{ and } \|f\| = \|f_0\|$
5. **Spectral Theorem**:
   $\text{Let } A \text{ be a self-adjoint (or normal) operator on a Hilbert space } \mathcal{H}.$
   $\text{ Then, there exists a spectral measure } E \text{ such that}$
   $A = \int_{\sigma(A)} \lambda \, dE(\lambda),$
   $\text{where } \sigma(A) \text{ is the spectrum of } A.$

## Linear Algebra

1. **Gradient Descent** 
  
   Gradient descent is a simple and effective algorithm for finding the minimum of a function. It is often used in machine learning to train models.
   
   $\theta_n+1 = \theta_n - \eta \nabla J(\theta_n)$
    where:
    
   $\theta$ is the parameter vector , 
   $J(\theta)$ is the loss function  ,
   $\eta$ is the learning rate,
   $\nabla J(\theta)$ is the gradient of the loss function with respect to the parameters
   2. 

 

<video src="https://github.com/jonas-kgomo/theorems/blob/main/media/videos/gradient/1080p60/FillByValueExample.mp4" width="480" height="270" controls></video>


