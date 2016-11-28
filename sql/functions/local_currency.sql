CREATE OR REPLACE FUNCTION public.local_currency(IN price_usd double precision, IN rate double precision)
RETURNS double precision
AS $function$
DECLARE
    result double precision;
BEGIN
    result := price_usd * rate;
    RETURN result;
END;
$function$ LANGUAGE 'plpgsql' IMMUTABLE;
