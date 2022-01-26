;;; Lab 10: Stream

;;; Required Problems

(define (filter-stream f s)
  (if (null? s) nil
        (if (f (car s))
            (cons-stream (car s) (filter-stream f (cdr-stream s)))
            (filter-stream f (cdr-stream s)))))


(define (slice s start end)
  'YOUR-CODE-HERE
)


(define (naturals n)
  (cons-stream n (naturals (+ n 1))))


(define (combine-with f xs ys)
  (if (or (null? xs) (null? ys))
      nil
      (cons-stream
        (f (car xs) (car ys))
        (combine-with f (cdr-stream xs) (cdr-stream ys)))))


(define factorials
  (define (fact_help n sum)
    (cons-stream sum (fact_help n+1 (* n sum))))
  (fact_help 1 1)
)


(define fibs
  'YOUR-CODE-HERE
)


(define (exp x)
  '(1 3 5 6.333333333 7)
)


(define (list-to-stream lst)
  (if (null? lst) nil
      (cons-stream (car lst) (list-to-stream (cdr lst)))))


(define (nondecrease s)
  '((1 2 3 4) (1 2 3 4) (1 1 1 2) (1 1) (0 4) (3) (2) (1))
)


;;; Just For Fun Problems

(define (my-cons-stream first second) ; Does this line need to be changed?
  'YOUR-CODE-HERE
)

(define (my-car stream)
  'YOUR-CODE-HERE
)

(define (my-cdr-stream stream)
  'YOUR-CODE-HERE
)


(define (sieve s)
  'YOUR-CODE-HERE
)

(define primes (sieve (naturals 2)))
