(define (double f)
  ;; Compose a function with itself (that is, 'double' it)
  (lambda (x) (f (f x))))

(define (compose f g)
  ;; Compose a function `f` with a function `g`, returning the composition
  ;; `x -> f(g(x))`
  (lambda (x) (f (g x))))

(define (repeated f n)
  ;; Return a procedure that computes the `n`th repeated application
  ;; of a function `f`
  (if (= n 1)
      f
      (repeated (compose f f) (- n 1))))

(define (average x y z)
  (/ (+ (x y z)) 3))

(define (smooth f)
  ;; Smooth a function `f` using a particular tolerance `dx`
  (let ((dx 0.0001))
       (lambda (x) (average (f (- x dx))
                            (f x)
                            (f (+ x dx))))))

(define (nfold-smooth f n)
  ;; Smooth a function `f`, `n` times
  ((repeated smooth n) f))
