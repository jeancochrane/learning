(define (for-each f lst)
  ;; Apply a function `f` to every item in the list `lst`, returning `true`
  (cond ((null? lst) #t)
        (else
          (f (car lst))
          (for-each f (cdr lst)))))

(define (for-each-map f lst)
  ;; Apply a function `f` to every item in the list `lst`, returning a list
  ;; of undefined elements with the same length as `lst`
  (map f lst))
