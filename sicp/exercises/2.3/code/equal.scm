(define (equal? a b)
  (cond ((and (null? a) (null? b)) true)
        ((and (list? a) (list? b))
           (and (equal? (car a) (car b))
                (equal? (cdr a) (cdr b))))
        ((and (symbol? a) (symbol? b))
           (eq? a b))))

;;; Tests
(newline)
(begin
  (display (equal? '(this is a list) '(this is a list)))
  ;;; Expected: #t
  (newline)
  (display (equal? '(this is a list) '(this (is a) list))))
  ;;; Expected: #f
