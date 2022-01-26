;;; Lab08: Scheme

(define (over-or-under a b)
  (if (>= a b) (if (> a b) 1 0) -1)
)


(define (make-adder n)
  (define (help x)
    (+ x n)
  )
  help
)


(define (composed f g)
  (define (help x)
    (f (g x))
  )
  help
)


(define (remainder a b)
  (- a (* b (quotient a b))))

(define (gcd a b)
  (if (= b 0) a (gcd b (remainder a b)))
)


(define lst
  (cons (cons 1 nil) (cons 2 (cons (cons 3 (cons 4 nil)) (cons 5 nil))))
)


(define (ordered s)
  (define (help s tmp)
    (if (null? (cdr s))
      (<= tmp (car s))
      (if (<= tmp (car s))
        (help (cdr s) (car s))
        #f
      )
    )
  )
  (help s (car s))
)
